class Solution:
    def mostCommonWord(self, paragraph: str, lst: List[str]) -> str:
        banned = set()
        for i in lst:
            banned.add(i.lower())
        start, end = 0, 0
        lst = []
        while end != len(paragraph):
            if not(97 <= ord(paragraph[end]) <= 122 or 65 <= ord(paragraph[end]) <= 90):
                if end != start:
                    lst.append(paragraph[start:end])
                    start = end + 1
                    end += 1
                else:
                    end += 1
                    start += 1
            else:
                end += 1
        if start != end - 1:
            lst.append(paragraph[start:end])
        print(lst)
        paragraph = lst
        dct = {}
        highest = 0
        word = ""
        for i in range(len(paragraph)):
            if paragraph[i] and 0 <= ord(paragraph[i][-1]) <= 26:
                paragraph[i] = paragraph[i][:-1]
            if paragraph[i].lower() in banned:
                continue
            if paragraph[i].lower() in dct:
                dct[paragraph[i].lower()] += 1
            else:
                dct[paragraph[i].lower()] = 1
            if dct[paragraph[i].lower()] > highest:
                highest = dct[paragraph[i].lower()]
                word = paragraph[i].lower()
        return word
