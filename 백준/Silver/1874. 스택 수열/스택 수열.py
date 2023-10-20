n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for number in sequence:
    while current <= number:
        stack.append(current)
        result.append("+")
        current += 1
    if stack and stack[-1] == number:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

for r in result:
    print(r)
