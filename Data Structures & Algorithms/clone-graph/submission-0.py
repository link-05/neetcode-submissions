"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque([node])
        clones = {node : Node(node.val)}
        while q:                
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clones[n].neighbors.append(clones[neighbor])
        return clones[node]

        