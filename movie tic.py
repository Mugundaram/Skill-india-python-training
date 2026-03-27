# Movie Ticket Pricing

age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif 5 <= age <= 12:
    price = 75
elif 13 <= age <= 60:
    price = 150
else:
    price = 100

print("Ticket Price: Rs.", price)