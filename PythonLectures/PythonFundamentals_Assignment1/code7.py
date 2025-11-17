'''
Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit.

Conversion formula:
FahrenheitTemp=(CelsiusTemp * (9/5))+32

'''
CelsiusTemp = input('Enter the temperature in Celsius : ')

CelsiusTemp = float(CelsiusTemp)

FahrenheitTemp = (CelsiusTemp * (9/5)) + 32

print('Temperature in Fahrenheit is : ', FahrenheitTemp)


