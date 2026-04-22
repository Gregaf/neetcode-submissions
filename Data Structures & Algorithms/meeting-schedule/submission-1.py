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
            current_interval = intervals[i]
            for j in range(i + 1, len(intervals), 1):
                comparison_interval = intervals[j]
                if current_interval.end > comparison_interval.start:
                    return False
        
        return True