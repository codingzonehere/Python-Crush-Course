'''
******************************************
**************TANVIR AHMED****************
****************CSE,DUET******************
******************************************
'''
#System of user input: input()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age = age + 2
print(f"Hello {name}")
print(f"Your age {age}")

#Very simple example.....!
#Exercise-01
adjective1 = input("Enter an adjective: ")
noun = input("Enter an noun: ")
verb = input("Enter an verb: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun} zoo.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}")

#Exercise-02
#Area Calculation:-
length = float(input("Enter the length of a rectange: "))
width = float(input("Enter the width of a rectange: "))
height = float(input("Enter the height of a rectange: "))

volume = length * width * height
print(f"The volume is: {volume} cm^m")

#Exercise-03
#Shoping Cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"You total is: ${total}")
print(f"You total is: ${round(total, 2)}")