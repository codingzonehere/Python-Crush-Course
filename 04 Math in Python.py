'''
******************************************
**************TANVIR AHMED****************
****************CSE,DUET******************
******************************************
'''
import math
friends = 10
#friends = friends + 1
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends * 3
#friends *= 3
#friends = friends / 2
#friends /= 2
#friends = friends ** 2
#friends **= 2
#friends = friends % 2
friends %= 2
print(friends)

x = 3.1416
y = 5
z = 10
a = -5
#result = round(x, 2)
#result = abs(a)
#result = pow(2,4)
#result = max(x, y, z)
result = min(x, y, z)
print(result)

# Use math library...
print(math.pi)
print(math.e)
#result = math.sqrt(x)
result = math.ceil(x)
print(result  )

#Get exercise........
#Exercise-01
radius = float(input("Enter the radius of a circule: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 3)}cm")

#Exercise-02
area = math.pi * pow(radius, 2)
print(f"The area is: {round(area, 3)}cm^2")

#Exercise-03
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C= {c}") 