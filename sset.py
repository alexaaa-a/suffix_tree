#!/usr/bin/env python3

"""
Suffix tree to search in dictionary
"""

from typing import List, Dict

class Node:
    def __init__(self):
        self.children = {}
        self.indexes = []

class SuffixTree:
    def __init__(self):
        self.root = Node()
        self.words = []

    def insert(self, word: str, index: int):
        for i in range(len(word)):
            current = self.root
            for char in word[i:]:
                if char not in current.children:
                    current.children[char] = Node()
                current = current.children[char]
                current.indexes.append(index)

    def search(self, substring: str) -> List[int]:
        current = self.root
        for char in substring:
            if char not in current.children:
                return []
            current = current.children[char]
        return current.indexes

class SSet:
    """String set. Should be based on Suffix tree"""

    def __init__(self, fname: str) -> None:
        """Saves filename of a dictionary file"""
        self.fname = fname
        self.tree = SuffixTree()

    def load(self) -> None:
        """
        Loads words from a dictionary file.
        Each line contains a word.
        File is not sorted.
        """
        with open(self.fname, 'r') as f:
            self.words = [line.rstrip() for line in f]
            for index, word in enumerate(self.words):
                self.tree.insert(word, index)

    def search(self, substring: str) -> List[str]:
        """Returns all words that contain substring."""
        indexes = self.tree.search(substring)
        return [self.words[i] for i in indexes]
