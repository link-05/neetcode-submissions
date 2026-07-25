class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
    
class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        target = self.trie
        for c in word:
            index = ord(c) - ord('a')
            if target.children[index] == None:
                target.children[index] = TrieNode()
            target = target.children[index]
        target.endOfWord = True
    def search(self, word: str) -> bool:
        target = self.trie
        for c in word:
            index = ord(c) - ord('a')
            if target.children[index] == None:
                return False
            target = target.children[index]
        return target.endOfWord

    def startsWith(self, prefix: str) -> bool:
        target = self.trie
        for c in prefix:
            index = ord(c) - ord('a')
            if target.children[index] == None:
                return False
            target = target.children[index]
        return True
        