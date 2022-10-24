import sys, heapq
input= sys.stdin.readline
minHeap = []

N = int(input())
for _ in range(N):
    num = int(input())
    
    if num == 0:
        if minHeap:
            print(heapq.heappop(minHeap))
        else:
            print(0)
    else:
        heapq.heappush(minHeap, num)
