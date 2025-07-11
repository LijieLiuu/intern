Dijkstra
====
**Dijkstra = BFS + Distance map + PQ**

Non-weighted graph - BFS

**Weighted graph - Dijkstra**

只要图中**不存在负权边**，Dijkstra 就能保证每次取出的节点的距离就是它的最终最短路径长度。其时间复杂度取决于优先队列的实现：用二叉堆(binary heap)为 O((V+E) log V)，用 Fibonacci 堆可降到 O(E + V log V)。


```python
from queue import PriorityQueue

# PriorityQueue - 最小堆结构
# q.put((priority, node)) - 插入元素，自动排序
# q.get()               - 取出最小 priority 元素
# q.empty()             - 判断队列是否为空

def Dijkstra(root):
    if root is None:
        return {}

    q = PriorityQueue()
    q.put((0, root))       # (distance, node)

    distances = {root: 0}   # distance map

    while not q.empty():
        curr_dist, node = q.get()

        # already known shortest path
        if curr_dist > distances[node]:
            continue

        for neighbour, weight in node.neighbours:  # (neighbour, weight)
            if neighbour is None:
                continue
            new_dist = curr_dist + weight
            if neighbour not in distances or new_dist < distances[neighbour]:
                distances[neighbour] = new_dist
                q.put((new_dist, neighbour))

    return distances

```
