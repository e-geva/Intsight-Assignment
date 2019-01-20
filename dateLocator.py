from myimports import *

#Mathud to extract the date from an item

def DateLocator(item):
    date =''
    numberOfReviews=''
    Months = ['Jan', 'Fab', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    findItems = item.find_elements_by_tag_name('span')
    for items in findItems:
        text = items.get_attribute('innerHTML')
        for month in Months:
            if text.find(month, 0, 3) != -1:
                date = text
        try:
            int(text)
            numberOfReviews = text
        except:
            pass
    return date,numberOfReviews