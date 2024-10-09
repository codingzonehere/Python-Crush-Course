'''
******************************************
**************TANVIR AHMED****************
****************CSE,DUET******************
******************************************
'''
# if = Do some code only IF some condition is true.
# Else do something else
age = int(input("Enter your age: "))

if age>=100:
    print("You are to old to sign up!")
elif age>=18:
    print("You are now signed up!")
elif age<0:
    print("You haven't born yet!")
else:
    print("You must be 18+ to sign up!")

# Another example:
response = input("Would you like food? (Y/N)")
if response == 'Y':
    print("Have some food!")
else:
    print("No food for you!")

# Another example:
name = input("Enter your name: ")
if name == '':
    print("You did not type your name!")
else:
    print(f"Hello {name}!")
    
# Another example:
online = True
if online:
    print("You are online!")
else:
    print("You are offline!!")