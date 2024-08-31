class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dct = collections.defaultdict(set)
        for key, val in reservedSeats:
            
            if val in {4,5}: 
                dct[key].add(0) 
                dct[key].add(1)
            elif val in {6,7}: 
                dct[key].add(1)
                dct[key].add(2)
            elif val in {8,9}: 
                dct[key].add(2)
            elif val in {2,3}:
                dct[key].add(0)
        res = 2*n
        # Iterate through the rows of seats
        for i in dct:
            # If a row has all three tallies, subtract two from the result
            if len(dct[i]) == 3: res -= 2
            # Otherwise, subtract one from the result
            else: res -= 1
        return res