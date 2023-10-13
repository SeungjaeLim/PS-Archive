def square_free_numbers(min_val, max_val):
    max_root = int((max_val)**0.5) + 1
    sieve = [1] * (max_val - min_val + 1)
    
    for i in range(2, max_root):
        square = i * i
        for j in range(max(square, (min_val + square - 1)//square * square), max_val+1, square):
            sieve[j - min_val] = 0
            
    return sum(sieve)

min_val, max_val = map(int, input().split())
print(square_free_numbers(min_val, max_val))
