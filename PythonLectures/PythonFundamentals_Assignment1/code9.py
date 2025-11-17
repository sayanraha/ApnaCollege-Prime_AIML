'''
Ask the user for: Principal (P), Rate (R), Time (T).
Convert all to float and compute simple interest:

SI = (P * R * T)/ 100

'''

P = float(input('Enter the principal amount P = '))
R = float(input('Enter the ROI R = '))
T = float(input('Enter the Time T = '))

SI = (P*R*T)/100

print("The SI is = ",SI)