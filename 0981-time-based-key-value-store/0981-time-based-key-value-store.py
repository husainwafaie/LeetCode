class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
            return
        self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        nums = self.map[key]
        l = 0
        r = len(nums) - 1
        if timestamp < nums[0][0] or len(nums) == 0:
            return ""
        curr = 0
        word = nums[curr][1]
        while r >= l:
            mid = (r + l) // 2
            if nums[mid][0] <= timestamp:
                if nums[mid][0] > nums[curr][0]:
                    curr = mid
                word = nums[curr][1]
                l = mid + 1
            else:
                r = mid - 1
        return word
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)