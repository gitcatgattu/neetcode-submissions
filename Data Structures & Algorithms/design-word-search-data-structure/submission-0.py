class TrieNode:
    def __init__(self):
        self.children={}
        self.EndOfWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.EndOfWord=True

    def search(self, word: str) -> bool:
        def dfs(i,root):
            cur=root
            for idx in range(i,len(word)):
                c=word[idx]
                if c==".":
                    for child in cur.children.values():
                        if dfs(idx+1,child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.EndOfWord
        return dfs(0,self.root)
