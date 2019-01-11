# program to check year is a leap or not

inp = int(input('Enter the year: '))
if inp % 4 == 0:
    if inp % 100 == 0:
        if inp % 400 == 0:
            print(str(inp),'is a leap year.')
        else:
            print(str(inp),'is not a leap year.')
    else:
        print(str(inp),'is a leap year.')
       
else:
    print(str(inp),'is not a leap year.')
