def create(create_namespace, namespace: str) -> None:
    global namespaces
    namespaces[create_namespace] = dict(parent=namespace, variables=[])


def add(namespace, variable: str) -> None:
    global namespaces
    namespaces[namespace]['variables'].append(variable)


def get(namespace, variable: str) -> str:
    global namespaces
    if variable in namespaces[namespace]['variables']:
        return print(namespace)
    elif namespace == 'global':
        return print('None')
    else:
        get(namespaces[namespace]['parent'], variable)


namespaces = {
    'global': {
        'parent': None,
        'variables': []
    }
}
for _ in range(int(input())):
    command = list(map(str, input().split()))
    if command[0] == 'create':
        create(command[1], command[2])
    if command[0] == 'add':
        add(command[1], command[2])
    if command[0] == 'get':
        get(command[1], command[2])
