n = int(input())
for i in range(n):
    eat, req = map(int, input().split())
    if eat < req:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")