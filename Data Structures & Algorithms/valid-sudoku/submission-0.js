class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {

        const rows={}
        const cols={}
        const squares={}
        for(let r=0;r<9;r++){
        for(let c=0;c<9;c++){
            const num=board[r][c]
            if(num===".") continue;

            if(!rows[r]) rows[r]=[]
            if(!cols[c]) cols[c]=[]
            const key=`(${Math.floor(r/3)},${Math.floor(c/3)})`
            if(!squares[key]) squares[key]=[]


            if(rows[r].includes(num)||cols[c].includes(num)||squares[key].includes(num)){
                return false
            }
            

            rows[r].push(num)
            cols[c].push(num)
            squares[key].push(num)





        }

        }
        return true
        
    }
}
