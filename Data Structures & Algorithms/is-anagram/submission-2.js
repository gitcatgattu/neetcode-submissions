class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const freq = new Array(26).fill(0);

    for (const char of s) {
        freq[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }

    for (const char of t) {
        const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
        freq[index]--;
        if (freq[index] < 0) {
            return false;
        }
    }

    return true;
}
}
