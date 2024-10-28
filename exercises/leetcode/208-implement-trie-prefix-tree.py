class Trie: 
    def __init__(self, isWord = False, children = []):
        self.isWord = isWord
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        cur = self
        for c in word: 
            pos = ord(c) - 97 
            if not cur.children[pos]:
                cur.children[pos]=Trie()
            cur = cur.children[pos]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            pos = ord(c) - 97
            if not cur.children[pos]:
                return False
            cur = cur.children[pos]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            pos = ord(c) - 97
            if not cur.children[pos]:
                return False
            cur = cur.children[pos]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
