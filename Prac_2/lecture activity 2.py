"""number of people average"""

number_of_people = 0
total = 0

age = int(input("Enter you age:"))
while age >= 0:
    total += age
    number_of_people += 1
    age = int(input("Enter you age:"))

if number_of_people == 0:
    print("Invalid")
    age = int(input("Enter you age:"))
else:
    print(total/number_of_people)


