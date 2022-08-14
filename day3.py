#1
sum_100 = 0
square_sum = 0
for i in range(100):
    sum_100 += i
    square_sum += i ** 2

print(square_sum - (sum_100 ** 2))

#2

#3
def palindrom(num):
    rev = 0
    num_ = num
    while num != 0:
        rev *= 10
        rev += num % 10
        num //= 10
    if rev == num_:
        return True
    return False

print(palindrom(121))
