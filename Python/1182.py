import sys
from itertools import combinations
input = sys.stdin.readline
n,s = list(map(int, input().split()))
numberList = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    subsequence = combinations(numberList, i)

    for j in subsequence:
        if sum(j) == s:
            cnt += 1

print(cnt)
