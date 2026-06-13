class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        ways = [0] * n
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n-1] + ways[n-2]
        # if n == 2: return 2 
        # s1 = 1
        # s2 = 1
        # for _ in range(2, n+1): c = s1 + s2, s2=s1,s1=c ; return s1
    