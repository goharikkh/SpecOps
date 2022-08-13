str = "Gohar is 20 year old"
l = len(str)
index = 2
for i in range(1, l):
    str = str[0: index:] + str[index + 1::]
    index += 2

print(str)