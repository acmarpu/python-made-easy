# module -1 logic

# calculator business logic

def Calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            raise "Error: Division by zero is not allowed."
    else:
        raise "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."