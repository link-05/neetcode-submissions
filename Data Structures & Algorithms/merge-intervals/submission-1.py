class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        # Set res init to interval 0 so there is always something to compare to
        res = [intervals[0]]
        # Comments are optimization
        # Using i in range is more optimal than interval
        for i in range(1, len(intervals)):
            # Sorted by min
            # if a numbers min is less than or equal to the max of the existing end value then take the max of the two max 
            # Instead of continuous check just use this as the initial value
            # if not res:
            #     res.append([interval[0], interval[1]]) or intervals[0][0] intervals[0][1]
            #     continue
            # currMin = res[-1][0]
            # currMax = res[-1][1]
            # intMin = interval[0] # intervals[i][0]
            # intMax = interval[1] # intervals[i][1]
            # Case for updating current interval - the current max is greater than or equal to intervals min 
            #    and the current max is less than the interval max
            if res[-1][1] >= intervals[i][0]:
                if res[-1][1] < intervals[i][1]:
                    res[-1][1] = intervals[i][1]
                    continue
                # currMax >= intMin:
                else:
                    continue
            res.append(intervals[i])
        return res