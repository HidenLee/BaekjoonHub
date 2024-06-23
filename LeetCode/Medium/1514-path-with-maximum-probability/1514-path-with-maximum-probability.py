class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        route = [[] for _ in range(n)]
        for idx, (fr,to) in enumerate(edges):
            route[fr].append((to,succProb[idx]))
            route[to].append((fr,succProb[idx]))
        maxprobability = [0.0 for _ in range(n)]
        maxprobability[start_node] = 1.0
        stack = [(-1.0,start_node)]
        while(stack):
            oprob, onode = heapq.heappop(stack)
            oprob *= -1
            if onode == end_node:
                return oprob
            
            for nnode, routeprob in route[onode]:
                nprob = oprob * routeprob
                if maxprobability[nnode] < nprob:
                    maxprobability[nnode] = nprob
                    heapq.heappush(stack,(-nprob,nnode))

        return 0.00000