from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        patterns=defaultdict(list)
        m=len(beginWord)# all words have same length
        for word in wordList:
            for j in range(m):
                pat=word[:j]+"*"+word[j+1:]
                patterns[pat].append(word)
        
        visit=set([beginWord])
        q=deque([beginWord])
        layer=1
        while q:
            for i in range(len(q)):
                cur_node=q.popleft()
            
                if cur_node==endWord:
                    return layer
                
                for j in range(m):
                    pat=cur_node[:j]+"*"+cur_node[j+1:]
                    for w in patterns[pat]:
                        if w not in visit:#w!=cur_node and 
                            q.append(w)
                            visit.add(w)

            layer+=1
            

        return 0


