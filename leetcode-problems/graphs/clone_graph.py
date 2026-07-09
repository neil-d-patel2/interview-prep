"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        q = deque([node])
        visited = {}
        visited[node] = Node(node.val)

        while q:
            ver = q.popleft()
            
            for neighbor in ver.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                visited[ver].neighbors.append(visited[neighbor])

        return visited[node]

