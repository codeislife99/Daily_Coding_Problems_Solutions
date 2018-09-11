def networkDelayTime(self, times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    print(graph)
    pq = [(0, K)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist: continue
        dist[node] = d
        for nei, d2 in graph[node]:
            if nei not in dist:
                heapq.heappush(pq, (d+d2, nei))