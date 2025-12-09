# ORGN: CMPS 3500
# ACTS: Activity 08
# NAME: Your Name
# DESC: Stack simulator with exception handling

MAX_SIZE = 10
stack = []

def isEmpty():
    return len(stack) == 0

def isFull():
    return len(stack) == MAX_SIZE

def size():
    return len(stack)

print("***********************************")
print("Stack Simulator")
print("***********************************")
print("Please only use digits from 0 to 9")
print("***********************************")
print("Please enter 'pop' for popping")
print("Please enter 'push' for pushing")
print("Please enter 'print' to print")
print("Please enter 'IsEmpty' to check if the stack is empty")
print("Please enter 'IsFull' to check if the stack is full")
print("Please enter 'size' to print the current size of the stack")
print("Please enter 'end' to terminate the program")

while True:
    command = input("...")

    if command == "push":
        if isFull():
            print("The stack is full, please pop an element to continue")
            continue

        value = input("Which number to push?... ")

        if not value.isdigit() or len(value) != 1:
            print("please enter only a 1 digit positive numbers")
            continue

        stack.append(value)

    elif command == "pop":
        if isEmpty():
            print("Cannot pop from an empty stack, please push some elements")
        else:
            print(stack.pop())

    elif command == "print":
        print(stack)

    elif command == "IsEmpty":
        if isEmpty():
            print("Stack is empty")
        else:
            print("Stack is not empty")

    elif command == "IsFull":
        if isFull():
            print("Stack is full")
        else:
            print("Stack is not full")

    elif command == "size":
        print(f"The current size of the stack is {size()}")

    elif command == "end":
        print("Thank you")
        break

    else:
        print("Unknown command")

