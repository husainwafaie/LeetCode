class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #return sorted(logs, key=lambda x:(x[0] != "l", x[5:]))
        lst1 = []
        lst2 = []
        for i in logs:
            if "".join(i.split(" ")[1:]).isdigit():
                lst2.append(i)
            else:
                lst1.append(i)
        lst1 = sorted(lst1, key=lambda x:[" ".join(x.split(" ")[1:]), " ".join(x.split(" ")[0])])
        lst1 += lst2
        return lst1