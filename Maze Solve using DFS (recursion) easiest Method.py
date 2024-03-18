from typing import List

class Solution:

    def Path(self, Maze: List[List[str]]) -> int:
        row_size = len(Maze)
        col_size = len(Maze[0])
        direction = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set()

        def dfs(row, col, step):
            if Maze[row][col] == "G":
                return step

            visited.add((row, col))    #marking as visit

            for row_inc, col_inc in direction:
                new_row = row + row_inc
                new_col = col + col_inc
                if (0 <= new_row < row_size) and (0 <= new_col < col_size) and Maze[new_row][new_col] != "0" and (new_row, new_col) not in visited:
                    result = dfs(new_row, new_col, step + 1)   #recursive call and increasing step every time untill goal found
                    if result != -1:
                        return result

            return -1

        for i in range(row_size):
            for j in range(col_size):
                if Maze[i][j] == "S":
                    return dfs(i, j, 0)

        return -1

Maze = [
    ["S", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "1", "1", "1", "0"],
    ["0", "0", "0", "1", "G"]
]


solution_obj = Solution()

result = solution_obj.Path(Maze)
if result >= 0:
    print("Minimum steps required:", result)
else:
    print("Can't reach the Goal")
