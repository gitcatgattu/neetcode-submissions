class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        # visit=set()
        # q=deque()
        # def check(r,c):
        #     if (r==0 or c==0 or r==ROWS or c==COLS) and board[r][c]=="O" and (r,c) not in visit:
        #         return False
        #     if r<1 or c<1 or r>=ROWS-1 or c>=COLS-1 or (r,c) in visit and board[r][c]=="O":
        #         return False
            
        #     board[r][c]="X"
        #     visit.add((r,c))
        #     return True
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return
            if board[r][c]=="O":
                board[r][c]="*"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or c==0 or r==ROWS-1 or c==COLS-1 :
                    if board[r][c]=="O":
                        dfs(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="*":
                    board[r][c]="O"

        # for 
        # while len(q)>0:
        #     for i in range(len(q)):
        #         r,c=q.popleft()
        #         if check(r+1,c) and check(r-1,c) and check(r,c+1) and check(r,c-1) :
        #             board[r][c]="X"

        