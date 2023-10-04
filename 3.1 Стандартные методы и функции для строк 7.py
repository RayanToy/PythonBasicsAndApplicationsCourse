s = input()
t = input()
count = 0
while s.find(t) != -1:
    if s.startswith(t):
        count += 1
    s = s[1:]
print(count)
