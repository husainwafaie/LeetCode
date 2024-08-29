class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lst = []
        if not digits:
            return lst
        
        dct = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def search(word, running, lst):
            if len(word) == 1:
                for i in dct[word]:
                    lst.append(running + i)
                return
            else:
                for i in dct[word[0]]:
                    search(word[1:], running + i, lst)
        
        search(digits, "", lst)
        return lst

        