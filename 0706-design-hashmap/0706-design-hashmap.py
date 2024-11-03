class Node:
    def __init__(self, key=-1, val=-1, nextt=None):
        self.key = key
        self.val = val
        self.next = nextt
class MyHashMap:

    def __init__(self):
        self.map = []

        for _ in range(1000):
            self.map.append(Node())

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        node = self.map[index]
        while node.next or node.key == key:
            if node.key == key:
                node.val = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.map[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        node = self.map[index]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


    def hash(self, key):
        return key % len(self.map)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)