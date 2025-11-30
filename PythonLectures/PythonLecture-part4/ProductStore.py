'''
Design and create an online store for Products(name,price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.

'''

class Product :
    count = 0
    def __init__(self,name,price): # this is called instance method
        self.name = name
        self.price = price
        Product.count += 1 #product count will always increase by one as soon as new products are being created.

    @staticmethod
    def prod_disc(price,discount):
        discounted_price = price - (price * discount/100)
        print(f"Discounted price for the product is {discounted_price}")



# pd1 = Product("HP-Laptop",45000)
# pd2 = Product("Samsumg Galaxy Mobile",23000)
# pd3 = Product("Washing machine",15000)

object_store = []

while True:
    name = input("Enter Product Name : ")
    if(name == "stop"):
        break
    price = float(input("Set Product Price : "))
    obj = Product(name,price)
    object_store.append(obj)


for i in object_store:
    print(i.name,i.price)
    i.prod_disc(price,8)
print(f"Total products present in the store is = {Product.count}")


    
