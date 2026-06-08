class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))

        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i

        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                parent[rootA] = rootB 

        for a, b in pairs:
            union(a, b)
        
        lstOfGraph = defaultdict(list)
        for i in range(n):
            lstOfGraph[find(i)].append(i)
        
        res = list(s)
        for graph in lstOfGraph.values():
            # we want to make sure the graph is maintained
            cycle = sorted(res[i] for i in graph)
            for i, val in enumerate(graph):
                res[val] = cycle[i]
        return "".join(res)

