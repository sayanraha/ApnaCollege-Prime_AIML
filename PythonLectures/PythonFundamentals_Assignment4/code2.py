'''
Create a class Book with the following attributes:

• title
• author
• list of reviews

And add methods to:-
• add a new review
• count reviews
• display all reviews

'''

class Book : 
    
    def __init__(self, title,author,reviews):
        self.title = title
        self.author = author
        self.reviews = reviews
    
    def AddReview(self,review):
        self.reviews.append(review)
        print("Review added Successfully")
    
    def CountReview(self):
        print(f"Total reviews are : {len(self.reviews)}")

    def DisplayReview(self):
        print(f"All reviews are : {self.reviews}")
    

bk1 = Book("Maths-12","Bk-Aggarwal",["Very intresting book for concepts"])

bk1.AddReview("Love this books..")
bk1.CountReview()
bk1.DisplayReview()