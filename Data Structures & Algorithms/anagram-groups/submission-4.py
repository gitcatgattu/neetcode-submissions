class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        for s in strs:
            A=[0]*26
            for ch in s:
                A[ord(ch)-ord('a')]+=1
            for i in range(26):
                A[i]=str(A[i])
            d["#".join(A)].append(s)
        return list(d.values())