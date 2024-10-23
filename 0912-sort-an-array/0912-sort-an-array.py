class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l):
            if len(l) == 1:
                return l
            mid = len(l) // 2
            return join(merge(l[:mid]), merge(l[mid:]))

        def join(l1, l2):
            p1 = 0
            p2 = 0
            lst = []
            while p1 < len(l1) or p2 < len(l2):
                if p1 == len(l1):
                    lst.append(l2[p2])
                    p2 += 1
                elif p2 == len(l2):
                    lst.append(l1[p1])
                    p1 += 1
                elif l1[p1] > l2[p2]:
                    lst.append(l2[p2])
                    p2 += 1
                else:
                    lst.append(l1[p1])
                    p1 += 1
            return lst

        return merge(nums)
