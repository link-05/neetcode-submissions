class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        for i in range(0, len(s2) - len(s1) + 1):
            if Counter(s1) == Counter(s2[l:r+1]):
                return True
            else:
                l+=1
                r+=1
        return False