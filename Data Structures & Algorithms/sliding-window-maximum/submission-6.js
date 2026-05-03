class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        let q=[nums[0]],l=0,r=0,output=[]
        for(;r<nums.length;r++){
            while(q[q.length-1]<nums[r]){
                q.pop()

            }
            if(r!=0)q.push(nums[r])
            if(r<k-1){
                continue
            }
            output.push(q[0])
            if(nums[l]==q[0]){
                q.shift()
            }
            l++
        }
        return output




    }
}
