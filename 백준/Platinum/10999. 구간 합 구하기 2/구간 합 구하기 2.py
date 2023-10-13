import sys

n = 0
elements = []
tree = []
lazy = []


def init(start, end, node):
    if start == end:
        tree[node] = elements[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]


def propagate(start, end, node):
    if lazy[node] != 0:
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        tree[node] += lazy[node] * (end-start+1)
        lazy[node] = 0


def update(start, end, node, left, right, dif):
    propagate(start, end, node)
    if end < left or right < start:
        return
    if left <= start and end <= right:
        lazy[node] = dif
        propagate(start, end, node)
        return

    mid = (start+end)//2
    update(start, mid, node*2, left, right, dif)
    update(mid+1, end, node*2+1, left, right, dif)

    tree[node] = tree[node*2] + tree[node*2+1]


def pSum(start, end, node, left, right):
    propagate(start, end, node)
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start+end)//2
    return pSum(start, mid, node*2, left, right) + pSum(mid+1, end, node*2+1, left, right)


if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    elements = [int(sys.stdin.readline()) for _ in range(n)]
    tree = [0] * (n * 4)
    lazy = [0] * (n * 4)

    init(0, n-1, 1)
    for _ in range(m+k):
        cmd = list(map(int, sys.stdin.readline().split()))
        if cmd[0] == 1:
            x, y, k = cmd[1:]
            update(0, n-1, 1, x-1, y-1, k)
        else:
            x, y = cmd[1:]
            print(pSum(0, n-1, 1, x-1, y-1))
