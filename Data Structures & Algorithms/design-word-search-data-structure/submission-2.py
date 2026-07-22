class TrieNode:
    def __init__(self):
        self.characters = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            
            cur = cur.characters[c]
        
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if len(word) == 0:
                return node.end
            
            c = word[0]
            if c == '.':
                for ch, nxt  in node.characters.items():
                    found = dfs(nxt, word[1:])
                    if found:
                        return True
                return False
            elif c not in node.characters:
                return False
            else:
                return dfs(node.characters[c], word[1:])

        return dfs(self.root, word)
        
