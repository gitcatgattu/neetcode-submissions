class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
      let Arr=[]
      let i=0,j=0
        while(i<nums1.length &&j<nums2.length){
            if(nums1[i]<nums2[j]){
                Arr.push(nums1[i])
                i++
            }
            else{
                Arr.push(nums2[j])
                j++
            }

        }
    while(i<nums1.length){
        Arr.push(nums1[i])
        i++
    }
    while(j<nums2.length){
        Arr.push(nums2[j])
        j++
    }
    let mid=Math.floor(Arr.length/2)
    if(Arr.length%2===0){
        return (Arr[mid]+Arr[mid-1])/2.0
    }
    else{
        return Arr[mid]
    }
    }
}
