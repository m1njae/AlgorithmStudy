import sys, heapq
input= sys.stdin.readline
absHeap = []

N = int(input())
for _ in range(N):
    num = int(input())
    
    if num == 0:
        if absHeap:
            print(heapq.heappop(absHeap)[1])
        else:
            print(0)
    else:
        heapq.heappush(absHeap, (abs(num), num))
