N, M, B = map(int, input().split())
terrain = [list(map(int, input().split())) for _ in range(N)]

min_time = float('inf')
best_height = -1

for h in range(257):  
    plus_blocks = 0
    minus_blocks = 0

    for i in range(N):
        for j in range(M):
            height_diff = terrain[i][j] - h
            if height_diff > 0:
                minus_blocks += height_diff
            else:
                plus_blocks -= height_diff

    total_blocks = B + minus_blocks 

    if total_blocks >= plus_blocks:
        time = plus_blocks + 2 * minus_blocks  
        if time < min_time or (time == min_time and h > best_height):
            min_time = time
            best_height = h

print(min_time, best_height)
