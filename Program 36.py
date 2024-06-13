user_input = input("Enter any value between 5 and 9: ")

# Check if the user wants to quit
if user_input == "quit":
    exit()

try:
    a = int(user_input)
except ValueError:
    raise ValueError("Invalid input. Please enter an integer between 5 and 9 or 'quit' to exit.")

# Check if the value is within the desired range
if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9")