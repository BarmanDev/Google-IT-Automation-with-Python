def divisible(max, divisor):
    count = 0
    for x in range(max+1):
        if x % divisor == 0:
            count += 1
    return count


print(divisible(100, 10))  # Debería ser 10
print(divisible(10, 3))  # Debería ser 3
print(divisible(144, 17))  # Debería ser 8
