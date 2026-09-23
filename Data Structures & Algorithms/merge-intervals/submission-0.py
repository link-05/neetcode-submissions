class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # Sorted by min
            # if a numbers min is less than or equal to the max of the existing end value then take the max of the two max 
            if not res:
                res.append([interval[0], interval[1]])
                continue
            currMin = res[-1][0]
            currMax = res[-1][1]
            intMin = interval[0]
            intMax = interval[1]
            # Case for updating current interval - the current max is greater than or equal to intervals min 
            #    and the current max is less than the interval max
            if currMax >= intMin and currMax < intMax:
                res[-1] = [currMin, max(intMax, currMax)]
                continue
            if currMax >= intMax and currMax >= intMin:
                continue
            res.append([intMin, intMax])
        return res