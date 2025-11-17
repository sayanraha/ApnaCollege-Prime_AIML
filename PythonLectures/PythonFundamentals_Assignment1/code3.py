# Ask the user to enter two integers and one float. Convert them all to floats and print their average.


n1 = int(input("Enter an integer value : "))
n2 = int(input("Enter an integer value : "))
n3 = float(input("Enter a float value : "))

avg = float(n1 + n2 + n3) / 3
print("Average is = ",avg)