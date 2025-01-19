"""
Breadth First Search (BFS)

Pseudocode: 

1. Enqueue the starting node
2. Dequeue
3. Is this the goal?
    a. If yes, finish
    b. If not, enqueue undiscovered neighbours to stack and update predecessors or visited node. (pushing as up, right, down, left)
4. Repeat until queue is empty

V = no of vertices and E = no of edges
TC = O(V+E)
SC = O(V)
"""

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

# prints a BFS of a graph
def bfs(node):

    # mark vertices as False means not visited
    visited = [False] * (len(graph))

    # make an empty queue for bfs
    queue = []

    # mark gave node as visited and add it to the queue
    visited.append(node)
    queue.append(node)

    while queue:
        # Remove the front vertex or the vertex at the 0th index from the queue and print that vertex.
        v = queue.pop(0)
        print(v, end = " ")

        # Get all adjacent nodes of the removed node v from the graph hash table.
        # If an adjacent node has not been visited yet,
        # then mark it as visited and add it to the queue.
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


if __name__ == "__main__":
    bfs('A')
