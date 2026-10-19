
def greetings(name, age=23):
    print(f"{name} is {age} years old.")

greetings("Abeera", 24)
greetings("Hooria")



def calculate_Val(a, b, operation):
    if operation == "add":
      return a+b


    elif operation == "subtract":
        return a-b

    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        if b == 0:
            print("Divide by zero")
        else:
            return a/b;


    else:
        return "Invalid operation"


print(calculate_Val(10, 5, "add"))
print(calculate_Val(10, 5, "subtract"))
print(calculate_Val(10, 5, "multiply"))
print(calculate_Val(10, 5, "divide"))
