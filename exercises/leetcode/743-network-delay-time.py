import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))

        def dijkstra():
            dist = [float("inf")] * (n+1)
            dist[k] = 0
            queue =[(0, k)]
            seen = set()
            min_times= 0
            while queue:  
                # min
                d, node = heapq.heappop(queue) 
                if d > dist[node]:
                    continue
                min_times = max(min_times, d)
                dist[node] = d 
                seen.add(node)
    
                for adj, dAdj in g[node]:
                    if adj not in seen:
                        heapq.heappush(queue, (dist[node] + dAdj, adj))

            return min_times if len(seen) == n else -1

        return dijkstra()
