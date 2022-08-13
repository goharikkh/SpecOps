def sum_of_digits(num):
    sum_ = 0
    while num != 0:
        sum_ += (num % 10)
        num //= 10
    return sum_


print(sum_of_digits(156))
