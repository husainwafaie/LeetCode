class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, r = 0, 3
        ret = ""
        while r != len(num) + 1:
            if num[l] == num[l+1] == num[l+2]:
                ret = max(ret, num[l:r])
            l += 1
            r += 1
        return str(ret)