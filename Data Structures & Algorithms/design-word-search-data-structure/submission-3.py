class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        def addWordHelper(node, word):
            if not word:
                return
            index = ord(word[0]) - ord('a')
            if not node.child[index]:
                node.child[index] = TrieNode()
            if len(word) == 1:
                node.child[index].endOfWord = True
            addWordHelper(node.child[index], word[1:])
        addWordHelper(self.root, word)

    def search(self, word: str) -> bool:
        self.foundWord = False
        def searchWordHelper(node, word) -> None:
            if not word:
                return
            candArr = [c for c in node.child if c]
            if word[0] == ".":
                if len(word) == 1 and len(candArr) > 0:
                    for cand in candArr:
                        if cand.endOfWord:
                            self.foundWord = True
                            return
                for cand in candArr:                        
                    searchWordHelper(cand, word[1:])
                return
            index = ord(word[0]) - ord('a')
            if not node.child[index]:
                return
            if len(word) == 1 and node.child[index].endOfWord:
                self.foundWord = True
                return
            searchWordHelper(node.child[index], word[1:])
        searchWordHelper(self.root, word)
        return self.foundWord

