class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ret = []
        start = newInterval[0]
        end = newInterval[1]
        for i in range(len(intervals)):
            if intervals[i][1] < start:
                ret.append(intervals[i])
            elif intervals[i][0] > end:
                ret.append([start, end])
                return ret + intervals[i:]
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
        ret.append([start, end])
        return ret