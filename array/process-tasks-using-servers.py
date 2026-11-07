# Process Tasks Using Servers
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Heap (Priority Queue)

"""
This algorithm simulates task processing using two min-heaps: `free_servers` (prioritized by server weight and index) and `busy_servers` (prioritized by task completion time). For each task, it advances time (fast-forwarding to the earliest server release time if all are busy), transfers newly freed servers back to the available pool, and assigns the highest-priority free server to the task. The time complexity is $\mathcal{O}((n + m) \log n)$ and the auxiliary space complexity is $\mathcal{O}(n + m)$, where $n$ is the number of servers and $m$ is the number of tasks.
"""

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = [0] * len(tasks)
        current_time = 0
        
        for j in range(len(tasks)):
            current_time = max(current_time, j)
            
            while busy_servers and busy_servers[0][0] <= current_time:
                _, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    _, weight, index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, index))
                    
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            heapq.heappush(busy_servers, (current_time + tasks[j], weight, index))
            
        return ans