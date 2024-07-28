class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 and len(matrix[0]) == 0:
            return []
        lst = []
        l, d, r, u = 0,0,0,1
        curr_x, curr_y = -1, 0
        char = "r"
        while True:
            if char == "r":
                while curr_x < len(matrix[0]) - r - 1:
                    curr_x += 1
                    lst.append(matrix[curr_y][curr_x])
                r += 1
                if curr_y +1 == len(matrix) - d:
                    return lst
                char = "d"
            elif char == "d":
                while curr_y < len(matrix) - d - 1:
                    curr_y += 1
                    lst.append(matrix[curr_y][curr_x])
                d += 1
                if curr_x == l:
                    return lst
                char = "l"
            elif char == "l":
                while curr_x > l:
                    curr_x -= 1
                    lst.append(matrix[curr_y][curr_x])
                l += 1
                if curr_y == u:
                    return lst
                char = "u"
            elif char == "u":
                while curr_y > u:
                    curr_y -= 1
                    lst.append(matrix[curr_y][curr_x])
                u += 1
                if curr_x + 1== len(matrix[0]) - r:
                    return lst
                char = "r"
