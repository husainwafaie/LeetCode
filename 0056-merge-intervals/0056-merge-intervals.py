class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        lst = []
        intervals = sorted(intervals, key = lambda x:x[0])
        while i < len(intervals):
            if i + 1 < len(intervals):
                if intervals[i][1] >= intervals[i+1][0]:
                    if intervals[i+1][0] > intervals[i][0]:
                        t = i
                    else:
                        t = i + 1
                    if intervals[i][1] > intervals[i+1][1]:
                        k = i
                    else:
                        k = i + 1
                    intervals[i+1] = [intervals[t][0],intervals[k][1]]
                    i += 1
                else:
                    lst.append(intervals[i])
                    i += 1
            else:
                lst.append(intervals[i])
                break
        return lst