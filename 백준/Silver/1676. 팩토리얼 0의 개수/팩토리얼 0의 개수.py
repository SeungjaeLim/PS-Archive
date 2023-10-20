def trailing_zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

n = int(input())

print(trailing_zeros(n))
