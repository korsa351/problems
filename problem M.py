def search_dupl_error(_error_, args):
    global errors, stack
    new_args = []
    if type(args) == str:
        args = [args]
    for _error in args:
        for parent in errors[_error]:
            if parent in stack:
                return print(_error_)
            new_args.append(parent)
    if not new_args:
        return stack.append(_error_)
    search_dupl_error(_error_, list(set(new_args)))


errors = {}
stack = []
for _ in range(int(input())):
    string = list(map(str, input().split()))
    if len(string) == 1:
        errors[string[0]] = []
    else:
        string.remove(':')
        errors[string[0]] = string[1:]
for total in range(int(input())):
    if total == 0:
        stack.append(str(input()))
        continue
    error = str(input())
    if error in stack:
        print(error)
        continue
    elif not errors[error]:
        stack.append(error)
        continue
    else:
        search_dupl_error(error, error)
