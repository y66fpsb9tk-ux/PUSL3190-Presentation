def fibonacci(n):
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result


print("First 10 Fibonacci numbers:")
print(fibonacci(10))# New Python file
