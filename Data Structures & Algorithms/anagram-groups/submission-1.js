class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    groupAnagrams(strs) {
       const map = new Map();
    
    for (const word of strs) {
        // Create a sorted key for the word
        const key = [...word].sort().join('');
        
        // Group words by their sorted key
        if (map.has(key)) {
            map.get(key).push(word);
        } else {
            map.set(key, [word]);
        }
    }
    
    // Return grouped anagrams
    return Array.from(map.values());
    }
}
