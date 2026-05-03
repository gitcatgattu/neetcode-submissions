class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
largestRectangleArea(heights) {
    let stack=[],area=0
    for(let i=0;i<heights.length;i++){

        let start=i

        while(stack.length>0 && stack[stack.length-1][1]>heights[i]){
            let[idx,height]=stack.pop()
            area=Math.max(area,(i-idx)*height)
            start=idx
        }
        stack.push([start,heights[i]])

    }
    for(let [i,h] of stack){
        area=Math.max(area,h*(heights.length-i))
    }
    return area











    }}