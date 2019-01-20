from myimports import *
from book import Book
from priceLocator import PriceLocator
from dateLocator import DateLocator
from starsLocator import StarLocator
from nameLocator import NameLocator

#Will iterate through the list and create a new one only with the data we need

def Iterator(list):

    BookList = []
    for item in list:
        name,author = NameLocator(item)
        price = PriceLocator(item)
        date, numberOfReviews = DateLocator(item)
        numberOfStars=StarLocator(item)
        book=Book(name,author,price,date,numberOfReviews,numberOfStars)
        BookList.append(book)
    return BookList

