class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        if(height.length===0) return 0
       
        let l = 0;
        let r = height.length - 1;
        let leftMax = height[l];
        let rightMax = height[r];
        let res = 0;
       while(l<r){
        if(leftMax<=rightMax){
            l+=1
            if(leftMax-height[l]>0)res+=leftMax-height[l]
            if(height[l]>leftMax)leftMax=height[l]
            
        }
        else{
            r-=1
            if(rightMax-height[r]>0)res+=rightMax-height[r]
            if(height[r]>rightMax)rightMax=height[r]
        }
       }
        return res;
    
    }
}
