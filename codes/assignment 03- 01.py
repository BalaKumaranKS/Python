# Program to print Fibonacci sequence

inp = int(input('Enter the value of terms: '))
n1 = 0
n2 = 1
count = 0
while count < inp:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count = count + 1
