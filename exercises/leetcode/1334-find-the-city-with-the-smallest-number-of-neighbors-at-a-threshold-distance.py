import heapq

class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        g = defaultdict(list)
        for f, t, w in edges:
            g[f].append((t, w))
            g[t].append((f, w))

        def dijkstra(source):
            dist = [float("inf")] * n
            dist[source] = 0
            queue = [(0, source)]
            count = 0
            while queue:
                d, node = heapq.heappop(queue)
                if d > dist[node]:
                    continue
                if d <= distanceThreshold:
                    count += 1
                for adj, weight in g[node]:
                    if dist[adj] > dist[node] + weight:
                        dist[adj] = dist[node] + weight
                        heapq.heappush(queue, (dist[adj], adj))
            return count

        min_neighbors = float("inf")
        best_city = -1

        for i in range(n):
            qty_cities = dijkstra(i)
            if qty_cities <= min_neighbors:
                min_neighbors = qty_cities
                best_city = i

        return best_city
