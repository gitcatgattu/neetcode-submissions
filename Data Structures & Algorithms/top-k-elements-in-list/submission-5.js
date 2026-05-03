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
       const res = [];
        for (let i = freq.length - 1; i > 0; i--) {
            for (const n of freq[i]) {
                res.push(n);
                if (res.length === k) {
                    return res;
                }
            }
        }



    }
}
