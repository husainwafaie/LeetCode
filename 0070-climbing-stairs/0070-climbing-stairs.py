class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        one = 1
        two = 1
        for i in range(n - 2, -1, -1):
            new = one + two
            two = one
            one = new
        return new