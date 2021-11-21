def C(a, b):
    if b == 0:
        return 1
    if b > a:
        return 0
    return C(a - 1, b) + C(a - 1, b - 1)


print(C(*map(int, input().split())))
