# First, we ask the user for their name using the input() function.
# The text inside the parentheses is the prompt that the user will see.
# Whatever the user types will be stored in the 'user_name' variable.
user_name = input("Please enter your name: ")

# Now, we use an f-string (formatted string literal) to easily combine
# the welcome message with the name the user provided.
# The 'f' before the opening quote tells Python to look for variables
# inside curly braces {} and replace them with their values.
print(f"Welcome {user_name}! I am new to AI")# This line prints a welcome message to Penny.
print("Welcome Penny! I am new to AI")