from collections import defaultdict
def depth_first_search(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end="->")
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

if __name__ == "__main__":
    graph = defaultdict(list)
    graph[0] = [4, 2]
    graph[1] = [2]
    graph[2] = [0,4]
    graph[3] = [4,6]
    graph[4] = [6]
    print("\ndepth first search traversal:")
    depth_first_search(graph, 2)
