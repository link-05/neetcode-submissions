"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        minVal = intervals[0].start
        for i in intervals:
            if i.start >= minVal: # Start greater than last end
                minVal = i.end
            else:
                return False
        return True