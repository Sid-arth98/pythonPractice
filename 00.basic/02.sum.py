def sum_of_evens(numbers):
    # Your code here
    sum = 0
    for i in numbers:
        if i%2 == 0:
            sum = sum + i
    return sum

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_evens(numbers_list)
print(f"Sum of even numbers: {result}")
