class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # getting char count of each each to list of anagrams
        for s in strs:
            count = [0] * 26 # a - z

            for c in s:
                count[ord(c) - ord("a")] += 1

            ans[tuple(count)].append(s)
             
        return list(ans.values())
