Priority Queue
===

常用function：

pq.put((priority score, item))

pq.get() # 拿出priority 和 item

pq.queue[0] # get top without pop


```python
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, "Mid-priority task"))
pq.put((1, "High-priority task"))
pq.put((3, "Low-priority task"))

print("Retrieving elements from PriorityQueue:")
while not pq.empty():
    priority, item = pq.get()
    print(f"Priority: {priority}, Item: {item}")
```
