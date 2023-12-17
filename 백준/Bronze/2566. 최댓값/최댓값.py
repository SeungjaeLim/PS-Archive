m = -1
mp = (-1, -1)
l = []
for i in range(9):
    t = list(map(int, input().split()))
    l.append(t)
for i in range(9):
    for j in range(9):
        if l[i][j] > m:
            m = l[i][j]
            mp = (i+1, j+1)
print(m)
print(mp[0], mp[1])