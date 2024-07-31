class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = []
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                lst.append(nums1[i])
            if i < len(nums2):
                lst.append(nums2[i])
        lst = sorted(lst)
        if len(lst) % 2 == 1:
            return lst[int((len(lst) / 2) - 0.5)]
        else:
            return (lst[int((len(lst) / 2) - 1)] + lst[int(len(lst) / 2)]) / 2