# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'    #

    cnt_possible = 1.0 * (x2 - x1) / (v2 - v1)
    # print(cnt_possible)
    if int(cnt_possible) == cnt_possible:
        return 'YES'
    else:
        return 'NO'


assert kangaroo(0, 3, 4, 2) == 'YES', 'test #1'
assert kangaroo(0, 2, 5, 3) == 'NO', 'test #2'