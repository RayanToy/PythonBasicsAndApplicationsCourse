namespaces = {
    'global': []
}


def get(var, namespace):
    parent = 'global'
    for key in namespaces.keys():
        if namespace in namespaces[key]:
            parent = key
    if var in namespaces[namespace]:
        return namespace
    else:
        if namespace == 'global' and var not in namespaces[namespace]:
            return None
        else:
            return get(var, parent)

+    """
+    Возвращает пространство имен заданной переменной в указанной иерархии пространств имен.
+
+    Параметры:
+        var (Any): Переменная, которую нужно найти.
+        namespace (str): Пространство имен, с которого начинается поиск.
+
+    Возвращает:
+        str или None: Пространство имен переменной, если она найдена, в противном случае None.
+    """

for i in range(int(input())):
    request = input().split()
    if request[0] == 'add':
        namespaces[request[1]].append(request[2])
    elif request[0] == 'create':
        namespaces[request[1]] = []
        namespaces[request[2]].append(request[1])
    elif request[0] == 'get':
        print(get(request[2], request[1]))