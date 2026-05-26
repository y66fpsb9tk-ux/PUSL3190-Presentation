print("Starting debug demo...")

numbers = [10, 5, 0, 2]

for num in numbers:
    print(f"\nCurrent value: {num}")

    try:
        result = 100 / num
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Debug Alert: Division by zero detected")
        print("Problematic value:", num)

print("\nDebug demo completed.")