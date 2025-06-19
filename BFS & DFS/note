The dffierence between DFS and BFS is append and appendleft(line 21)
==================================================================
BFS:
from collections import deque

# deque - double end queue
# dq.append()      - 往右 append
# dq.appendleft()  - 往左 append
# dq.pop()         - pop 最右边的
# dq.popleft()     - pop 最左边的

def BFS(root):
    if root is None:
        return []

    dq = deque([root])
    visited = {root: True}   # 存储已访问的节点
    result = []

    while len(dq):
        top = dq.pop()
        result.append(top)
        for neighbour in top.neighbours:
            if neighbour is not None and neighbour not in visited:
                dq.appendleft(neighbour)
                visited[neighbour] = True

    return result
==================================================================

Container is important!!!
The only difference between BFS/DFS is its container. BFS uses queue to contain to-be-visited nodes while DFS uses stack to contain to-be-visited nodes. 
For a more generalized traversal method, the key difference is still the container!!! No matter how fancy the traversal method is, we can always select a container to do the traversal.

Level-order traversal - “level list”
BFS - queue
DFS - stack
A* Search - priority queue
……

For DFS, it can also be written in recursion since its utilizing stack as its container. Sometimes recursion version is easier. Sometimes using stack is easier.
