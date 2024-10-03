def total_button_presses(m):
    # Define the number of presses for each letter
    button_presses = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4,
        'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9, 'J': 10, 'K': 11, 'L': 12,
        'M': 13, 'N': 14, 'O': 15, 'P': 16,
        'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24,
        'Y': 25, 'Z': 26
    }

    total_presses = 0

    # Convert message to uppercase and iterate through each character
    for char in m.upper():
        if char in button_presses:
            total_presses += button_presses[char]

    return total_presses


message = input("Hello! Enter the message whose number of buttons pressed u want to check. ")
result = total_button_presses(message)
print(result)
