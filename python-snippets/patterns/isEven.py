#I'm creating a function that checks if an number is even or not
def is_even(number):
    if number % 2 ==0:
        return True
    else:
        return False
#Example usage
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False

#create input from user to check if the number is even or not
user_input = int(input("Enter a number: "))
if is_even(user_input):
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")

