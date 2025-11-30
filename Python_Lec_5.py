# Find the word "Python" from the sample.txt and print its line number.

data = True
line = 1
with open("sample.txt","r") as f :
    while data:
        data = f.readline()
        if ("Python" in data):
            print(f"Word found at line {line}")
            break

        line += 1
        