res = {
    "black": [0, 1],
    "brown": [1, 10],
    "red": [2, 100],
    "orange": [3, 1000],
    "yellow": [4, 10000],
    "green": [5, 100000],
    "blue": [6, 1000000],
    "violet": [7, 10000000],
    "grey": [8, 100000000],
    "white": [9, 1000000000]
}
tot_res = 0
for i in range(3):
    s = input()
    if i < 2:
        tot_res += res[s][0] * 10 ** (1 - i)
    else:
        tot_res *= res[s][1]
print(tot_res)
