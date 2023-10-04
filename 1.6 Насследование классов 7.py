'''
Вам дано описание наследования классов в следующем формате.

имя класса 1 : имя класса 2 имя класса 3 ... имя класса k

Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass
Класс A является предком класса B, если

A = B
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C
Например:

class B(A):
    pass

class C(B):
    pass

# A -- предок С
Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:

Создавать классы не требуется.

Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате имя класса 1 имя класса 2.

Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

** Sample Input**:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No
'''

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
