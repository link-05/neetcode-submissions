class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tLen = len(temperatures)
        res = [0] * tLen
        for i in range(tLen-2, -1, -1):
            nextVal = i + 1
            while nextVal < tLen and temperatures[nextVal] <= temperatures[i]:
                if res[nextVal] == 0:
                    nextVal = tLen
                    break
                nextVal += res[nextVal]
            if nextVal < tLen:
                res[i] = nextVal - i
        return res