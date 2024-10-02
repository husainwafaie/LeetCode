from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        queue = deque()
        queue.append(0)
        for i in range(1, k):
            while len(queue) != 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        lst = [nums[queue[0]]]
        r = k
        l = 1
        while r != len(nums):
            if len(queue) == k:
                queue.popleft()

            while queue and queue[0] < l:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)

            lst.append(nums[queue[0]])
            r += 1
            l += 1
        return lst