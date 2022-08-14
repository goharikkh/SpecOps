#1
nums = open("1ex", 'r')
count = 0
for line in nums:
    nums_str = line.split(" ")
    nums_int = list(map(int, nums_str))
    count += sum(nums_int)


print(count)

#2
txt = open('2ex', 'r').read()
txt_new= open('2ex_new', 'w')
txt_titled = txt.title()
txt_new.write(txt_titled)

#3
lst = [1, 2, 2, 3, 3, 3, 4, 4, 5]
dup = {}
unique_lst = set(lst)
for i in unique_lst:
    dup[i] = lst.count(i)
print(dup)

#4
f = open('2ex', 'r').read()
count = 0
for char in f:
    if char.isprintable():
        count += 1
print(count)

#5
str = "Gohar is 20 year old"
l = len(str)
index = 2
for i in range(1, l):
    str = str[0: index:] + str[index + 1::]
    index += 2

print(str)

#6
def word_counter(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_counter('barev barev  dzez'))

#7
def square(num):
    return num ** 2


lst = [2, 14, 5, -3]
lst_squared = list(map(square, lst))
lst_squared.sort()
print(lst_squared)


#8
def sum_of_digits(num):
    sum_ = 0
    while num != 0:
        sum_ += (num % 10)
        num //= 10
    return sum_


print(sum_of_digits(156))

#9
def dif(num):
    sum_ = 0
    mult = 1
    while num != 0:
        sum_ += (num % 10)
        mult *= (num % 10)
        num //= 10
    return mult - sum_


print(dif(43))

#10
def foo(start, end):
    count = 0
    while start <= end:
        if start %2 != 0:
            count += 1
        start += 1
    return count

print(foo(5, 12))
