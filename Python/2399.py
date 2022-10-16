import sys

input = sys.stdin.readline
n = int(input())
numberList = list(map(int, input().split()))
numberList.sort()

halfSum = 0

for i in range(n):
    halfSum += numberList[i] * (2*i - n + 1)

result = halfSum * 2

print(result)
