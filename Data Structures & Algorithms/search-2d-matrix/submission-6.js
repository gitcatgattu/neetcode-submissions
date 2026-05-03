class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        if(target<matrix[0][0]||target>matrix[matrix.length-1][matrix[0].length-1]) return false
        let l=0,r=matrix.length-1,midR=0
        if(matrix.length>1){

        for(midR=Math.floor((l+r)/2);l<=r;midR=Math.floor((l+r)/2)){
            if(matrix[midR][0]<=target && target<=matrix[midR][matrix[0].length-1]){
                break
            }
            else if(matrix[midR][0]>target){
                r=midR-1
            }
            else if(matrix[midR][matrix[0].length-1]){
                l=midR+1
            }
            

        }
        }
        l=0,r=matrix[0].length-1
        for(let midC=Math.floor((l+r)/2);l<=r;midC=Math.floor((l+r)/2)){
            if(matrix[midR][midC]===target){
                return true
            }
            else if(matrix[midR][midC]>target){
                r=midC-1
            }
            else{
                l=midC+1
            }
    }
    return false
    }
}
