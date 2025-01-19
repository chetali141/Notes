"""
Depth First Search (DFS)

Pseudocode: 

1. Add starting node to the stack
2. Pop the stack
3. Is this the goal?
    a. If yes, finish
    b. If not, push undiscovered neighbours to stack and update predecessors or visited node. (pushing as up, right, down, left)
4. Repeat until stack is empty

V = no of vertices and E = no of edges
TC = O(V+E)
SC = O(V+E)
"""


def dfs(node, graph, visited, component):
    component.append(node)  # Store answer
    visited[node] = True  # Mark visited

    # Traverse to each adjacent node of a node
    for child in graph[node]:
        if not visited[child]:  # Check whether the node is visited or not
            dfs(child, graph, visited, component)  # Call the dfs recursively


if __name__ == "__main__":

    # Graph of nodes
    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    node = 0  
    visited = [False]*len(graph)  # Make all nodes to False initially i.e. not visited
    component = []
    dfs(node, graph, visited, component)  # Traverse to each node of a graph
    print(f"Following is the Depth-first search: {component}")  # Print the answer
