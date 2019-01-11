# Program to check Armstrong number

inp = int(input('Enter the number: '))
sum = 0
n = inp
while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10
if sum == inp:
    print(str(inp),'is an Armstrong number')
else:
    print(str(inp),'is not an Armstrong number')
