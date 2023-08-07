def solution(sizes):
    for i, v in enumerate(sizes):
        if v[0] <= v[1]:
            sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]
    l = [list(x) for x in zip(*sizes)]
    maxL = max(l[0])
    maxS = max(l[1])
    answer = maxL * maxS
    return answer