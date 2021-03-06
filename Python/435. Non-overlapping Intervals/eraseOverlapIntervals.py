# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted([(x.end, x.start) for x in intervals])
        count, end = 0, float('-inf')
        for e, s in intervals:
            if s >= end:
                end = e
                count += 1
        return len(intervals) - count
