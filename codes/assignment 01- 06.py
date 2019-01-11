# Program to calculate future value

value01 = int(input('Enter the Principal amountin Rs: '))
value02 = int(input('Enter the Rate of interest in %: '))
value03 = int(input('Enter the number of years: '))
value04 = value02 / 100
value05 = value04 + 1
value06 = value05 ** value03
value07 = value01 * value06
print('The future value in Rs',str(value07))
