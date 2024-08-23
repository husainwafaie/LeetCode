class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = []
        n1, n2 = 0, 0
        while True:
            if n1 == len(nums1):
                lst += nums2[n2:]
                break
            if n2 == len(nums2):
                lst += nums1[n1:]
                break
            if nums1[n1] > nums2[n2]:
                lst.append(nums2[n2])
                n2 += 1
            else:
                lst.append(nums1[n1])
                n1 += 1
        print(lst)
        if len(lst) % 2 == 0:
            return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2
        return lst[int(len(lst) / 2)]