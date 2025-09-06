import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        stops = defaultdict(int)

        flightDict = defaultdict(list)
        for subSrc, subDst, price in flights:
            flightDict[subSrc].append((subDst, price))
        print(flightDict)

        pq = [(0, -1, src)]

        while pq:
            curPrice, pathStops, node = heapq.heappop(pq)
            print(f"node: {node} curPrice: {curPrice}, pathStops: {pathStops}")

            if pathStops > k:
                continue
            
            if node == dst:
                return curPrice

            if stops[node] == 0 or stops[node] > pathStops:
                stops[node] = pathStops
                for subDst, price in flightDict[node]:
                    heapq.heappush(pq, (curPrice + price, pathStops + 1, subDst))
                
                print(pq)
        
        return -1
    
sol = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

print(sol.findCheapestPrice(n, flights, src, dst, k))
