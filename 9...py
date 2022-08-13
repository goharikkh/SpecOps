def dif(num):
    sum_ = 0
    mult = 1
    while num != 0:
        sum_ += (num % 10)
        mult *= (num % 10)
        num //= 10
    return mult - sum_


print(dif(43))