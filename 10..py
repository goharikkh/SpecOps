def foo(start, end):
    count = 0
    while start <= end:
        if start %2 != 0:
            count += 1
        start += 1
    return count

print(foo(5, 12))