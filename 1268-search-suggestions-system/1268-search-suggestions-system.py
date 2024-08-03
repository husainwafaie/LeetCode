class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        lst = []
        for i in range(1, len(searchWord)+1):
            lst2 = []
            first = 0
            last = len(products) - 1
            key = searchWord[:i]
            while first <= last:
                mid = int((first + last) / 2)
                if products[mid][:i] == key:
                    while mid - 1 > -1 and products[mid-1][:i] == key:
                        mid -= 1
                    for j in range(mid, len(products)):
                        if products[j][:i] == key:
                            lst2.append(products[j])
                        else:
                            break
                        if len(lst2) == 3:
                            break
                    break
                elif products[mid][:i] > key:
                    last = mid - 1
                else:
                    first = mid + 1
            lst.append(lst2)
        return lst
            