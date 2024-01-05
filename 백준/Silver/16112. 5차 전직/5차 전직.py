import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().rstrip().split())
stone = list(map(int, input().rstrip().split()))
stone.sort()

exp = 0
quest = 0
for i in range(n):
    exp += quest * stone[i]
    if quest < k:
        quest += 1
print("%d" % exp)