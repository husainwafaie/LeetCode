from collections import deque
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        lst = [tops[0], bottoms[0]]
        lowest = -1
        while len(lst) != 0:
            num = lst[-1]
            if tops.count(lst[-1]) >= bottoms.count(lst[-1]):
                target = tops
                helper = bottoms
            else:
                target = bottoms
                helper = tops
            count = 0
            m = True
            for i in range(len(target)):
                if target[i] == num:
                    continue
                elif helper[i] == num:
                    count += 1
                else:
                    m = False
                    break
            if m:
                if lowest == -1 or lowest > count:
                    lowest = count
            lst.pop()
        return lowest
            
        