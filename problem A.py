classes = {}
for _ in range(int(input())):
    string = list(map(str, input().split()))
    try:
        string.remove(':')
    except ValueError:
        pass
    if string[0] not in classes:
        classes[string[0]] = []
        classes[string[0]] += string[1:]
    else:
        classes[string[0]] += string[1:]
for _ in range(int(input())):
    request = list(map(str, input().split()))
    queue = classes[request[1]][::]
    if request[0] == request[1]:
        print('Yes')
        continue
    if not queue:
        print('No')
        continue
    while queue:
        _class = queue.pop()
        if _class == request[0]:
            print('Yes')
            break
        elif request[0] in classes[_class]:
            print('Yes')
            break
        else:
            queue += classes[_class]
        if not queue:
            print('No')
            break
