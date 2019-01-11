#program to calculate value of n+nn+nnn

n = int(input('Enter the value of n: '))
s1 = n * n
s2 = s1 * n
sum = n + s1 + s2
print(sum)
