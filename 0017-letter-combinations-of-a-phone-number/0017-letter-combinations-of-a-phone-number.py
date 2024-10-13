class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dct = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        lst = []

        def dfs(index, word):
            if index == len(digits):
                lst.append(word)
                return
            for letter in dct[digits[index]]:
                dfs(index + 1, word + letter)
        
        dfs(0, "")
        return lst
        