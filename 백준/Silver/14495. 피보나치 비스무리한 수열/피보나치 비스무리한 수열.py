mem = [0] * 117
def fibo(n):
    if n < 4:
        return 1
    if mem[n] == 0:
        res = fibo(n-1) + fibo(n-3)
        mem[n] = res
    return mem[n]

n = int(input())
print(fibo(n))