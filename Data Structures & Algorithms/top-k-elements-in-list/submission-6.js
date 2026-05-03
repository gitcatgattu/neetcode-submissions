class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
         const freq = Array.from({ length: nums.length + 1 }, () => []);//nums.leng bcoz if all elements of nums are same
        console.log(freq)
        let count={}
        for(let num of nums){
            count[num]=(count[num]||0)+1

        }
        for(const [key,value] of Object.entries(count)){
            freq[value].push(parseInt(key))
        }
        let ans=[]
        let x=0
        for(let i=0;i<k;i++){
            while(freq[nums.length-x].length===0 && x<=nums.length){
                x+=1
            }
            let ele=freq[nums.length-x].pop()
            ans.push(ele)
        }
return ans|| []




    }
}
