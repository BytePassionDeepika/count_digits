def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

number_to_count = int(input("Enter the number:"))
result = count_digits(number_to_count)

print(f"Number: {number_to_count}")
print(f"Number of Digits: {result}")
