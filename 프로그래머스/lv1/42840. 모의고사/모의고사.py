def solution(answers):
    answer = []
    
    ans1 = [1, 2, 3, 4, 5] * 2000
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i, v in enumerate(answers):
        ans1[i] -= v
        ans2[i] -= v
        ans3[i] -= v
    
    col = []
    col.append(ans1.count(0))
    col.append(ans2.count(0))
    col.append(ans3.count(0))
    
    maxcol = -1
    for i, v in enumerate(col):
        if v > maxcol:
            maxcol = v
            answer = []
            answer.append(i+1)
        elif v == maxcol:
            answer.append(i+1)
    
    return answer