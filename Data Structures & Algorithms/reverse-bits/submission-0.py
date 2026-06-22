class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            ith = ((n>>i) & 1)
            if ith:
                res |= (1 << (31 - i))
        return res