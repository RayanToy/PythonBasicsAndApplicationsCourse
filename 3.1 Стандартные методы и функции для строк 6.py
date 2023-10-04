s = input()
a = input()
b = input()
count = 0
while s.find(a) >= 0 and count < 1000:
    s = s.replace(a, b)
    count += 1
print('Impossible' if count == 1000 else count)
