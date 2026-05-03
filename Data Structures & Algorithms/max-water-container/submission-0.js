class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l=0,r=heights.length-1,max_area=0
        while(l<r){
            let curr_h=Math.min(heights[l],heights[r])
            let curr_w=r-l
            let curr_area=curr_h*curr_w
            if(heights[l]<heights[r]) l+=1
            else r-=1
            max_area=Math.max(max_area,curr_area)

        }
        return max_area
    }
}
