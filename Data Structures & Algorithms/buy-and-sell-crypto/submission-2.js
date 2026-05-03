class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
    let l=0,r=prices.length-1,max=0
    let maxRight=[],minLeft=[],a=prices[l]
    for(let p of prices){
        minLeft.push(a)
        if(p<a){
            a=p
        }

    }   
   console.log(minLeft)
    a=prices[r]  
    for(let i=prices.length-1;i>=0;i--){
        if(prices[i]>a)a=prices[i]
        maxRight.unshift(a)

    }
    console.log(maxRight)
    for(let i=0;i<prices.length;i++){
        max=Math.max(max,maxRight[i]-minLeft[i])
    }
    return max

    }
}
