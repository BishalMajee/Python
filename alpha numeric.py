def sum_of_numbers_in_string(s):
    # Initialize sum
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the digit character to an integer and add to total_sum
            total_sum += int(char)
    
    return total_sum

def main():
    # Input alphanumeric string from user
    alphanumeric_input = input("Enter an alphanumeric string: ")
    
    # Calculate the sum of all numeric digits in the input string
    result = sum_of_numbers_in_string(alphanumeric_input)
    
    # Print the result
    print(f"The sum of all numeric digits in the input is: {result}")

if __name__ == "__main__":
    main()
