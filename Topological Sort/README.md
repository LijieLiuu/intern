Topological Sort
==============================
How to traverse a DAG in a way similar to BFS?  **Topological Sort!**

```python
from collections import deque

def topological_sort(nodes):
    # nodes is a list of all nodes, each node has .neighbours attribute
    indegree = {node: 0 for node in nodes}

    for node in nodes:
        for neighbour in node.neighbours:
            if neighbour is not None:
                indegree[neighbour] += 1

    dq = deque([node for node in nodes if indegree[node] == 0])
    result = []

    while len(dq):
        top = dq.pop()
        result.append(top)

        for neighbour in top.neighbours:
            if neighbour is not None:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    dq.appendleft(neighbour)

    if len(result) != len(nodes):
        raise ValueError("Graph has a cycle or disconnected component")

    return result
```
![项目示意图](images/Screenshot 2025-06-25 at 23.02.23.png)

Differences between Topological Sort and BFS
===================================
Topological Sort has to maintain an **indegree table** (or map) for all nodes.
