def getNum(number):
    value1 = input("Enter number"+str(number)+": ")
    try:
        return float(value1)
    except:
        print("Invalid input. Please enter a numeric value.")
        return getNum(number)
    
val1 = getNum(1)
val2 = getNum(2)
operation = input("Enter operation (+, -, *, /): ")

if(operation == '+'):
    result = val1 + val2
    print(result)
elif(operation == '-'):
    result = val1 - val2
    print(result)
elif(operation == '*'):
    result = val1 * val2
    print(result)
elif(operation == '/'):
    if val2 != 0:
        result = val1 / val2
        print(result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")