class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = [0] * 26 # 23 value character array 
        offset = ord('a')
        for c in s: 
            dict[ord(c) - offset]+=1
        for c in t:
            dict[ord(c) - offset]-=1
        return set(dict) == {0}

        