#Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”.

n = input("Enter a number (or Quit): ")

while n != "Quit":
    n = float(n)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

    n = input("\nEnter a number (or Quit): ")

print("Program ended.")

      