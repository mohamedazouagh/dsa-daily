"""0025 - Implement Trie (medium · trie / prefix tree)

Build a word store with three operations: insert(word), search(word) which
is True only for words that were inserted exactly, and starts_with(prefix)
which is True when any inserted word begins with prefix. The empty prefix
matches as soon as anything is stored; the empty word can itself be inserted.

Idea: a tree of nested dicts, one edge per character. Shared prefixes share
nodes. Each node has an end-of-word flag, which is what separates "app" being
a stored word from "app" only being the start of "apple".

Time O(L) per operation for a word or prefix of length L · Space O(total
characters inserted)
"""
from __future__ import annotations


class Trie:
    def __init__(self) -> None:
        self._root: dict = {}
        self._end = object()  # sentinel key, cannot clash with a character

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._end] = True

    def _walk(self, text: str) -> dict | None:
        node = self._root
        for ch in text:
            node = node.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and self._end in node

    def starts_with(self, prefix: str) -> bool:
        node = self._walk(prefix)
        return node is not None and bool(node)
