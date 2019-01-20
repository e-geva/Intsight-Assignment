from myimports import *
from iterator import Iterator
from listLocator import ListLocator
from searcher import Searcher
from flipPage import FlipPage
from addToCart import AddToCart
from insertListToDB import InsertListToDB

#Run example assigment for IntSight by Erez Geva

browser= webdriver.Chrome('C:/Users/erez2/PycharmProjects/intsight/venv/chromedriver.exe')
browser.get('https://www.amazon.com/')
timeout = 10
pages = 4
search = 'software testing'
BookList=[]

#First add to cart and assas if item was added

Searcher(browser,timeout,search)
addToCartTest=AddToCart(browser,timeout)

#Create a list of the firs 4 pages a search bring back

browser.get('https://www.amazon.com/')
Searcher(browser,timeout,search)
for page in range(0,pages):
	items=ListLocator(browser,timeout)
	BookList.append(Iterator(items))
	FlipPage(browser,timeout)

#insert List to DB mySQL server

InsertListToDB(BookList)
print("Bye Bye")