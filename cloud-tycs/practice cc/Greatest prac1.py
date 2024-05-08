from zeep import Client

client = Client('http://localhost:10000/?wsdl')

numbers = [10, 20, 30]  # Add more numbers here

largest_number = numbers[0]
for number in numbers[1:]:
    if number > largest_number:
        largest_number = number

result = largest_number
print(f"The largest number is: {result}")




###First run the soap server prac1 ki file then this 