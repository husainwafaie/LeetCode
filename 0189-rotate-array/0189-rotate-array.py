class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k = k % len(nums)
        # for _ in range(k):
        #     temp, temp2 = nums[0], nums[1]
        #     for i in range(len(nums)):
        #         nums[(i+1) % len(nums)] = temp
        #         temp = temp2
        #         temp2 = nums[(i+2) % len(nums)]
        # return
        # k = k % len(nums)
        # count = 0
        # temp = nums[0]
        # temp2 = nums[k]
        # num = k
        # while count < len(nums):
        #     nums[num] = temp
        #     temp = temp2
        #     num = (num+k) % len(nums)
        #     temp2 = nums[num]
        #     count += 1
        dct = {}
        for i in range(len(nums)):
            dct[i] = nums[i]
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = dct[i]