s = input()
t = input()
total = 0
while s:
    if len(s) < len(t):
        break
    if s.startswith(t):
        total += 1
    s = s[1:]
print(total)
