# Program tofind triangle type

inp01 = int(input('Enter the triangle length in X axis: '))
inp02 = int(input('Enter the triangle length in Y axis: '))
inp03 = int(input('Enter the triangle length in Z axis: '))

if inp01 == inp02 == inp03:
    print('The triangle is Equilateral')
elif inp01 == inp02 or inp02 == inp03 or inp03 == inp01:
    print('The triangle is Isosceles')
else:
    print('The triangle is Scalene')
