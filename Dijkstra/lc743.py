from queue import PriorityQueue


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if times == None:
            return -1

        q = PriorityQueue()
        q.put((0, k))

        distance = {k: 0}

        while not q.empty():
            cur_dis, node = q.get()

            if cur_dis > distance[node]:
                continue

            for s, t, weight in times:
                if s == node:
                    if t == None:
                        continue
                    new_dis = cur_dis + weight

                    if t not in distance or new_dis < distance[t]:
                        distance[t] = new_dis
                        q.put((new_dis, t))

        if len(distance) < n:
            return -1
        return max(distance.values())
