class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # A dictionary that defaults to list
        for word in strs:
            w2 = ''.join(sorted(word))
            res[w2].append(word)
        return list(res.values())