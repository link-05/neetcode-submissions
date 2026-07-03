class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        maxSeq = 0

        for i in range(len(s)):
            # if c in dic and in bound
            if s[i] in dic and dic[s[i]] >= left:
                # Move left boundary to track next non dup
                left = dic[s[i]]+1
            dic[s[i]] = i

            maxSeq = max(maxSeq, i - left + 1)
        return maxSeq
    