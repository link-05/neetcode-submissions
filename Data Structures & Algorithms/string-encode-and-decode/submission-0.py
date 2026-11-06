class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        # Encode encoded with length # string
        res = []
        i = 0
        while i < len(s):
            j = i
            # Looped count of what the length of string is 
            while s[j] != '#':
                j += 1
            # Grab the size of the string from i to j count
            length = int(s[i:j])
            # 
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res 