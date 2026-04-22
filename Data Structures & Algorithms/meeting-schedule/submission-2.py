"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        intervals = sorted(intervals, key=lambda x:x.start)

        # Brute force approach
        for i in range(len(intervals) - 1):
            interval_curr = intervals[i]
            interval_next = intervals[i + 1]

            if interval_curr.end > interval_next.start:
                return False
        
        return True
                    
            