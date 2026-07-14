from collections import deque


graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}


def topological_sort(graph):
    """
    graph: dict[str, list[str]]
    returns: list[str]
    """
    q = deque()
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        q.appendleft(node) 

    for node in graph:
        if node not in visited:
            dfs(node)

    return q

def main():
    
    graph = {
        "A": ["C"],
        "B": ["C", "D"],
        "C": ["E"],
        "D": ["F"],
        "E": ["H", "F"],
        "F": ["G"],
        "G": [],
        "H": []
    }

    q = topological_sort(graph)    
    print(q)

if __name__ == "__main__":
    main()

