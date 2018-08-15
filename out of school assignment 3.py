#This is a calculator to compute area of certain shapes

#Algorithm
#Collect name
#Display Instruction
#input the desired shape to be computed
#calculate based on the input
#calculation collects desired variable and produces answers

#import math library to use pi
import math

name = str(input('\n what is your name? \n'))
print ('\n Dear', name, 'This calculator is designed to compute the area of sector\n trapezoid\n cylinder\n square\n triangle \n')
choice = str (input('Enter the name of shape to compute:'))

#to calculate only sector
if choice == 'sector':
    radius = eval(input('radius of the sector is: '))
    angle = eval(input('angle which sector subtends is: '))
    sectorArea = (0.5 * math.pi * radius**2 * angle)
    print('The area of the sector is:', round(sectorArea,2))
    print ('Thanks follow me on twitter @princecoker')

#to calculate only square
elif choice == 'square':
    length = eval(input('What is the length of the square: '))
    squareArea = (length**2)
    print('The area of the Square is: ', round(squareArea,2))
    print ('Thanks follow me on twitter @princecoker')

#to calculate only trapezoid    
elif choice == 'trapezoid':
    length1 = eval(input('value of the 1st lenght is: '))
    length2 = eval(input('value of the 2nd lenght is: '))
    height = eval(input('Height of trapezoid is: '))
    trapezoidArea = (0.5 * (length1 + length2) * height)
    print('The area of the Trapezoid is: ', round(trapezoidArea,2))
    print ('Thanks follow me on twitter @princecoker')

#to calculate only triangle
elif choice == 'triangle':
    base = eval(input('Base of the traingle is: '))
    height = eval(input('Height of triangle is: '))
    triangleArea = (0.5 * base * height)
    print('The area of the Triangle is: ', round(triangleArea,2))
    print ('Thanks follow me on twitter @princecoker')

#to calculate only cylinder
elif choice == 'cylinder':
    radius = eval(input('radius of the cylinder is: '))
    height = eval(input('Height of cylinder is: '))
    cylinderArea = (2 * maths.pi * radius * height) + (2 * maths.pi * radius**2)
    print('The area of the Cylinder is: ', round(cylinderArea,2))
    print ('Thanks follow me on twitter @princecoker')

#to display alternative response where wrong shape is typed
else:
    print ('you have entered the wrong shape')
    print (' Good Bye. Thanks follow me on twitter @princecoker')
