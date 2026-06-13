class Solution:
    def isHappy(self, n: int) -> bool:
        def sumS(x:int):
            sum = 0
            while x > 0:
                sum += (x%10) **2
                x = x // 10
            return sum
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumS(n)

        return True