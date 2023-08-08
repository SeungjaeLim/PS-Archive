v = int(input())
n = int(input())
s = 0

for i in range(n):
    price, num = map(int, input().split())
    s += price * num
    
if v == s:
    print('Yes')
else:
    print('No')