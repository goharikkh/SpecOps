nums = open("1ex", 'r')
count = 0
for line in nums:
    nums_str = line.split(" ")
    nums_int = list(map(int, nums_str))
    count += sum(nums_int)


print(count)