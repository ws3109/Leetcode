# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for inter in intervals[1:]:
            if inter.start > result[-1].end:
                result.append(inter)
            else:
                result[-1].end= max(result[-1].end, inter.end)
        return result
