class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res=[]
        sub=[]
        dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def dfs(i):
            if i==len(digits):
                res.append("".join(sub[:]))
                return
            st=dic[digits[i]]
            for char in st:
                sub.append(char)
                dfs(i+1)
                sub.pop()
            
        dfs(0)
        return res