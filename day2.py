#1
def str_move(str, num):
    if num == len(str):
        return str
    elif num < len(str):
        return str[-num:] + str[0:num + 1]
    return str_move(str, num - len(str))

print(str_move('hello', 2))

#2
sum = 0
a, b = 1, 2
while a < 4000000:
    a, b = b, a + b
    if a % 2 == 0:
        sum += a

print(sum)

#3
sum = 0
for i in range(1, 1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print(sum)
