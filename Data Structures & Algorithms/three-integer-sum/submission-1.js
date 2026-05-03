class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums=nums.sort((a,b)=>a-b)
        let ans=[]
        for(let i=0;i<nums.length;i++){

            if(nums[i]>0 || i>0 && nums[i-1]==nums[i]){
                continue
            }
            
            let l=i+1,r=nums.length-1
            while(l<r){
                let sum=nums[l]+nums[r]+nums[i]
                if(sum>0){
                    r-=1
                }
                else if(sum<0){
                    l+=1
                }
                else{
                    ans.push([nums[l],nums[r],nums[i]])
                    l+=1
                    while(nums[l-1]==nums[l]){
                        l+=1
                    }

                }
            
            }
        }
    
    return ans
        
    }
}
