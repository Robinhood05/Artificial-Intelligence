import collections
from typing import List

class Solution:

    def Path(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque()
        visited = set()

        directions = [(1,0),(-1,0),(0,-1),(0,1)] #Possible moving steps up down left and right

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "S":           #checking the 2d lists and finding start positions
                    queue.append((row, col, 0))
                    visited.add((row, col))       #making the start position as visited
                    break                     #exiting from nested for loop

        while queue:                          #starting from S untill list is empty
            cur_row, cur_col, steps = queue.popleft()        #1 steps and marking current rows and col

            if grid[cur_row][cur_col] == "G":               #if Goal is find returning the steps
                return steps
            else:                                          #else
                for row_inc, col_inc in directions:        #moving all possible directions
                    temp_row=cur_row
                    temp_col=cur_col
                    new_row = cur_row + row_inc            #new row will be present row + possible directions vector
                    new_col = cur_col + col_inc

                    if (0 <= new_row < rows) and (0 <= new_col < cols) and grid[new_row][new_col] != "0":     #checking if list not out of bounds and not blocked by 0

                        if (new_row, new_col) not in visited:               #if new row and col not visited making it visited
                            print("From "+str(temp_row), temp_col)      #printing current position
                            print("To "+str(new_row), new_col)          #printing newx movement

                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col, steps + 1))      #increment the steps with 1 and adding the new row and col in the queue

        return -1     #if solution not found returning -1

# Define the grid
grid = [
    ["S", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "1", "1", "1", "0"],
    ["0", "0", "0", "1", "G"]
]


solution_obj = Solution()

# Call the function
result = solution_obj.Path(grid)
if result>0:
    print("Minimum steps required:", result)

else :
  print("Can't Reach the Goal")
     
