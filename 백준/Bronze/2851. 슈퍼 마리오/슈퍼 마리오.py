score = 0
for i in range(10):
    n = int(input())
    if score + n > 100:
        if score + n - 100 <= 100 - score:
            score += n
            break;
        break;
    else:
        if score < 100:
            score += n
print(score)