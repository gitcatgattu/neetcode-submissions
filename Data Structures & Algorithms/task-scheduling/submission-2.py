class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        task=[-c for c in count.values()]
        heapq.heapify(task)
        q=deque()
        time=0
        while task or q:
            time+=1
            if task:
                task_freq=1+heapq.heappop(task)
                if task_freq:
                    q.append([task_freq,time+n])
            if q and q[0][1]==time:
                heapq.heappush(task,q.popleft()[0])

        return time