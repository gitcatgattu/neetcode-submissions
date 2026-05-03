class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let map={}
        for(let num of nums){
            if(map[num]!==undefined) return true
            map[num]=num

        }
        return false
    }
}
