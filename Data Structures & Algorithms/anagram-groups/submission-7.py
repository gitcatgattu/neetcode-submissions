class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            
            arr=[0]*26
            for i in range(len(s)):
                arr[ord(s[i])-97]+=1
            key="".join([str(i)+"#" for i in arr])
            hashmap[key].append(s)
        
        return list(hashmap.values())