
Input= {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': ['L', 'M', 'N'],
    'J': ['R'],
    'K': ['S'],
    'N': ['S'],
    'K':['O','P']
}

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1): 
        visited = set()  
        if dls(start, goal, depth, visited): #recursive call untill goal found
            return True
    return False

def dls(start2, goal, depth, visited):
    if start2 == goal:
        print("Goal reached:", node)
        return True
    if depth <= 0:
        return False
    if start2 in visited:
        return False
    
    visited.add(start2)
    
    for neighbor in Input.get(start2, []):
        if dls(neighbor, goal, depth - 1, visited):
            return True
    
    return False

start_node = 'A'
goal_node = 'R'
max_depth = 6  # As max llimit not given lets assume it

print("Searching for path from", start_node, "to", goal_node, "with maximum depth", max_depth)
if iddfs(start_node, goal_node, max_depth):
    print("Path found!")
else:
    print("Path not found within the maximum depth.")
