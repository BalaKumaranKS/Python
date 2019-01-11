# Program to convert celcius to farenheit
data = input('Enter type of conversion: ')
if data == ('C-F'):
    inp01 = int(input('Enter temperature in Celcius: '))
    solve = (inp01 * 1.8)
    cal01 = (solve + 32)
    print('The temperature in Farenheit is',str(cal01))
    
else:
   inp02 = int(input('Enter temperature in Farenheit: '))
   solve02 = (inp02 - 32)
   cal02 = (solve02 * 0.56)
   print('The temperature in Celcius is',str(cal02))
