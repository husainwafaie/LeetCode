class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dct = {}
        self.last_used = 0
        self.smallest = 1
        self.dct2 = {}

    def get(self, key: int) -> int:
        if key in self.dct:
            del self.dct2[self.dct[key][1]]
            self.dct2[self.last_used + 1] = key
            while self.smallest not in self.dct2:
                self.smallest += 1
            self.dct[key] = [self.dct[key][0], self.last_used + 1]
            self.last_used += 1
            return self.dct[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            if self.dct[key][1] == self.smallest:
                self.smallest += 1
                del self.dct2[self.smallest - 1]
            else:
                del self.dct2[self.dct[key][1]]
            self.dct[key] = [value, self.last_used + 1]
            self.dct2[self.last_used + 1] = key
            self.last_used += 1
            while self.smallest not in self.dct2:
                self.smallest += 1
        else:
            if self.size != self.capacity:
                self.dct[key] = [value, self.last_used + 1]
                self.dct2[self.last_used + 1] = key
                self.size += 1
                self.last_used += 1
            else:
                del self.dct[self.dct2[self.smallest]]
                del self.dct2[self.smallest]
                self.dct[key] = [value, self.last_used + 1]
                self.dct2[self.last_used + 1] = key
                while self.smallest not in self.dct2:
                    self.smallest += 1
                self.last_used += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)