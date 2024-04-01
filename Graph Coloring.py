class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def greedy_coloring(self):
        colors = {}  
        for vertex in self.vertices:
           
            colors[vertex] = None
        
       
        def is_safe(vertex, color):
            for neighbor in self.adjacency_list[vertex]:
                if colors[neighbor] == color:
                    return False
            return True
        
        available_colors = ['red', 'blue', 'yellow', 'black', 'pink', 'green']  
        
      
        for vertex in self.vertices:
            for color in available_colors:
                if is_safe(vertex, color):
                    colors[vertex] = color
                    break
        
        return colors


graph = Graph(['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria'])

graph.add_edge('Western Australia', 'Northern Territory')
graph.add_edge('Western Australia', 'South Australia')
graph.add_edge('Northern Territory', 'South Australia')
graph.add_edge('Northern Territory', 'Queensland')
graph.add_edge('South Australia', 'Queensland')
graph.add_edge('South Australia', 'New South Wales')
graph.add_edge('South Australia', 'Victoria')
graph.add_edge('Queensland', 'New South Wales')
graph.add_edge('New South Wales', 'Victoria')

colors = graph.greedy_coloring()

for vertex, color in colors.items():
    print(f"Vertex {vertex} is colored with Color {color}")

num_colors = len(set(colors.values()))
print(f"Minimum number of colors needed: {num_colors}")
