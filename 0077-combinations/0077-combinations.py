class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        lst = []
        
        def helper(rem, l, start):
            

            if rem == 0:
                lst.append(l.copy())
                return
            for i in range(start, n+1):
                l.append(i)
                helper(rem - 1, l, i + 1)
                l.pop()
            
        for i in range(1, n+1):
           helper(k - 1, [i], i + 1)
        
        return lst