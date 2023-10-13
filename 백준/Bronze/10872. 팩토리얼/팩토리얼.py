n = int(input())
tot = n
while n > 1:
    tot = tot * (n-1)
    n = n - 1
if tot == 0:
    print(1)
else:
    print(tot)