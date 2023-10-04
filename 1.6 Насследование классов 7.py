def graph(parent, child):
    if parent == child and parent in d and child in d:
        return True
    for iteration in d[child]:
        if iteration == parent:
            return True
        if parent not in d[child]:
            if graph(parent, iteration):
                return True
    return False
+    """
+    Определяет, существует ли путь от заданного родительского узла к заданному дочернему узлу в графе.
+
+    Параметры:
+        parent (любой): Родительский узел.
+        child (любой): Дочерний узел.
+
+    Возвращает:
+        bool: True, если существует путь от родительского узла к дочернему узлу, иначе False.
+    """


d = {}
for i in range(int(input())):
    Inheritance = input().split()
    d[Inheritance[0]] = Inheritance[2:]
for i in range(int(input())):
    check = input().split()
    if check[0] in d and check[1] in d:
        print('Yes' if graph(check[0], check[1]) else 'No')
    else:
        print('No')
