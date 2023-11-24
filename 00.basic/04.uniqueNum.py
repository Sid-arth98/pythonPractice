
"""
def find_unique_elements(input_list):
    # Your code here
    return list(set(input_list))
"""
def find_unique_elements(input_list):
    seen = set()
    unique = []
    for i in input_list:
        if i not in seen:
            unique.append(i)
            seen.add(i)
    return unique        

# Example usage:
numbers = [2, 3, 4, 3, 6, 2, 7, 8, 9, 9, 7]
unique_numbers = find_unique_elements(numbers)
print(f"Original List: {numbers}\nUnique Elements: {unique_numbers}")
