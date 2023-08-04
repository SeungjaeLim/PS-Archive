l = list(map(int, input().split()))

if l[0] == l[1] and l[1] == l[2]:
    print(10000 + l[0]*1000)
elif l[0] == l[1]:
    print(1000 + l[0] * 100)
elif l[1] == l[2]:
    print(1000 + l[1] * 100)
elif l[2] == l[0]:
    print(1000 + l[2] * 100)
else:
    print(max(l)*100)
    