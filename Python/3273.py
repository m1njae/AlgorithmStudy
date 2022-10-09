import sys

input = sys.stdin.readline
n = int(input())
numberList = list(map(int, input().split()))
x = int(input())

numberList.sort()
start = 0
end = n-1

count = 0
while start < end:
    current = numberList[start] + numberList[end]
    if current == x:
        count += 1
        start += 1
    elif current < x:
        start +=1
    elif current > x:
        end -=1

print(count)
