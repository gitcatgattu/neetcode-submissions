class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
      let i=0
      let pre=1
      let output=[]
      while(i<nums.length){
        output.push(pre)
        pre*=nums[i]
        i+=1
      }
      let post=1
      let j=nums.length-1
      while(j>=0){
        output[j]*=post
        post*=nums[j]
        j-=1
      }
      return output
    }
}
