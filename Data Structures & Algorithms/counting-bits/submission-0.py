class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n + 1)
        offset = 1
        for i in range(1, len(ret)):
            if offset * 2 == i:
                offset = i
            ret[i] = 1 + ret[i-offset]
        return ret
            
