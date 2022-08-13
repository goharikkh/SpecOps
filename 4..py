f = open('2ex', 'r').read()
count = 0
for char in f:
    if char.isprintable():
        count += 1
print(count)
