n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(0)
for _ in range(m):
    i, j, k = map(int, input().split())
    for t in range(i-1, j):
        l[t] = k
for _ in l:
    print(_, end = ' ')