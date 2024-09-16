library = {
    1: "Book 1", 2: "Book 2", 3: "Book 3", 4: "Book 4", 5: "Book 5",
    6: "Book 6", 7: "Book 7", 8: "Book 8", 9: "Book 9", 10: "Book 10"
}

code = int(input("Enter the desired Book ID: "))

# Use .items() to get key-value pairs from the dictionary
for k, v in library.items():
    if k == code:
        print(f"The name of the book is {v.title()}.")
        break  # Exit loop once the book is found

else:
    print("Book ID not found.")
