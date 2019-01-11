# Program to calculate no of digit and letter

inp = input('Enter the string: ')
digits = 0
letters = 0
for i in inp:
    if (i.isdigit()):
        digits = digits + 1
    else:
        letters = letters + 1

print('The number of digits is:',(digits))

print('The number of letters is:',(letters))








