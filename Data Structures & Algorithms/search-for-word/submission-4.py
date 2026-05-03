class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,curr_idx):
            if curr_idx==len(word):
                return True
            if 1==len(word) and board[r][c]==word[curr_idx]:
                return True 
            if board[r][c]==word[curr_idx]:
                board[r][c]="*"
                rows=[1,0,-1,0]#up,right,down,left
                cols=[0,1,0,-1]
                res=False
                for i in range(4):
                    row=rows[i]+r
                    col=cols[i]+c
                    if 0<=row and 0<=col and row<len(board) and col<len(board[0]):
                        if dfs(row,col,curr_idx+1):
                            res= True
                            
                board[r][c]=word[curr_idx]
                return res
            else:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False