class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = []
        lst2 = []
        running = ""
        for i in range(len(version1)):
            if version1[i] == ".":
                lst1.append(int(running))
                running = ""
            else:
                running += version1[i]
            if i == len(version1) - 1:
                lst1.append(int(running))
        running = ""
        for i in range(len(version2)):
            if version2[i] == ".":
                lst2.append(int(running))
                running = ""
            else:
                running += version2[i]
            if i == len(version2) - 1:
                lst2.append(int(running))
        for i in range(max(len(lst1), len(lst2))):
            if i >= len(lst1):
                if lst2[i] > 0:
                    return -1
            elif i >= len(lst2):
                if lst1[i] > 0:
                    return 1
            elif lst1[i] > lst2[i]:
                return 1
            elif lst2[i] > lst1[i]:
                return -1
        return 0