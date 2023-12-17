import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = [i+1 for i in range(n)]

for k in range(m):
    i, j = map(int, input().split())
    tmp = l[i-1:j]
    tmp.reverse()
    for t in range(i-1, j):
        l[t] = tmp[t - i + 1]

for k in l:
    print(k, end = ' ')