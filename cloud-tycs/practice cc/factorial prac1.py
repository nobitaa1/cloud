from zeep import Client

client = Client('http://localhost:10000/?wsdl')





number = 5  # Change this to the number you want to find the factorial of

factorial = 1
for i in range(1, number + 1):
    factorial *= i

result = factorial
print(f"The factorial of {number} is: {result}")


###First run the soap server prac1 ki file then this 

