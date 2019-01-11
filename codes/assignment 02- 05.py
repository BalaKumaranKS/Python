# Program to check largest number
inp01 = int(input('Enter the First Number: '))
inp02 = int(input('Enter the Second Number: '))
inp03 = int(input('Enter the Third Number: '))
if(inp01>inp02 and inp03):
    print('The largest number is',inp01)
elif(inp02>inp03 and inp01):
    print('The largest number is',inp02)
else:
    print('The largest number is',inp03)
    
