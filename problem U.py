s = input()
a = input()
b = input()
total = 0
while True:
    if total > 1000:
        print("Impossible")
        break
    if a not in s:
        print(total)
        break
    else:
        s = s.replace(a, b)
        total += 1
