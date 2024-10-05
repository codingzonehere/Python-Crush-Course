'''
******************************************
**************TANVIR AHMED****************
****************CSE,DUET******************
******************************************
'''
'''
variable: A container for a value (string, integer, float, boolean)
          A variable behaves as if it was the value it contains.
'''
#String..........
first_name = "bro"
email = "mdtanvir@gmail.com"
print(f"Hello {first_name}")
print(f"Email: {email}")

#Integer..........
age = 25
quality = 5
print(f"You are age {age} years old")
print(f"You are buying {quality} items")

#Float..........
price = 99.99
gpa = 3.56
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")

#Boolean..........
is_student = True
print(f"Are you student {is_student}")

if is_student:
    print("You are student")
else:
    print("You are NOT student")