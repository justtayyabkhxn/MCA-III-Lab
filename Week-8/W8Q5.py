def separate_numbers_and_alphabets(input_string):
    L1 = []  # List to hold numbers
    L2 = []  # List to hold alphabets

    for char in input_string:
        if char.isdigit():
            L1.append(char)
        elif char.isalpha():
            L2.append(char)

    return L1, L2

input_string = input("Enter a string containing alphabets and numbers: ")
numbers, alphabets = separate_numbers_and_alphabets(input_string)
    
print("List of numbers (L1):", numbers)
print("List of alphabets (L2):", alphabets)
