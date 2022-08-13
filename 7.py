def square(num):
    return num ** 2


lst = [2, 14, 5, -3]
lst_squared = list(map(square, lst))
lst_squared.sort()
print(lst_squared)
