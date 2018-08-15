# computes area of a sector

import math
print ('this calculator computes the area of a sector')
radius = eval(input('radius of the sector is: '))
angle = eval(input('angle which sector subtends is: '))
sectorArea = (0.5 * math.pi * radius**2 * angle)
print('The area of the sector is:', round(sectorArea,2))
print ('Thanks follow me on twitter @princecoker')
