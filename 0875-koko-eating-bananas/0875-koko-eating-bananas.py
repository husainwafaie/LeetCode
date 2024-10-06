class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        dct={}

        def check(num, h):
            if num == 0:
                return False
            steps = 0
            for i in piles:
                steps += math.ceil(i / num)
                if steps > h:
                    return False
            return True

        while r >= l:
            mid = int((r + l) / 2)
            state = check(mid, h)
            dct[mid] = state
            if not state and mid + 1 in dct and dct[mid+1]:
                return mid + 1
            elif state and mid -1 in dct and not dct[mid -1]:
                return mid
            elif state:
                r = mid - 1
            else:
                l = mid + 1
        return -1