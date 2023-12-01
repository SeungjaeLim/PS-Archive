ans = int(input())
p = list(map(int, input().split()))
num = 0

for i in p:
    if i == ans:
        num += 1
        
print(num)
