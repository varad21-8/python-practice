def greet(name):
    return f"Hello, {name}! This code is from the second branch."


name = input("Enter your name: ")
message = greet(name)

print(message)