def divide_numbers(a, b):
    result = a / b
    return result


numbers = [10, 5, 0, 2]

for num in numbers:
    output = divide_numbers(100, num)
    print(f"100 / {num} = {output}")