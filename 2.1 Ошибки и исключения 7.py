def check_exceptions(parent, child):
    if parent == child and parent in exceptions_inheritance and child in exceptions_inheritance:
        return True
    for iteration in exceptions_inheritance[child]:
        if iteration == parent:
            return True
        if parent not in exceptions_inheritance[child]:
            if check_exceptions(parent, iteration):
                return True
    return False

    """
    Проверяет, является ли родительское исключение предком дочернего исключения.

    Параметры:
        parent (Exception): Родительское исключение для проверки.
        child (Exception): Дочернее исключение для проверки.

    Возвращает:
        bool: True, если родительское исключение является предком дочернего исключения, иначе False.
    """


exceptions_inheritance = {}
try_exceptions = []
another_exceptions = []
for i in range(int(input())):
    Inheritance = input().split()
    exceptions_inheritance[Inheritance[0]] = Inheritance[2:]
for i in range(int(input())):
    try_exception = input()
    try_exceptions.append(try_exception)
for exception in reversed(range(len(try_exceptions))):
    for catch_exception in range(exception):
        if (check_exceptions(try_exceptions[catch_exception], try_exceptions[exception]) and
                try_exceptions[exception] not in another_exceptions):
            another_exceptions.append(try_exceptions[exception])
for i in reversed(another_exceptions):
    print(i)
