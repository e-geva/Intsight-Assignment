from myimports import *

#Mathod will serch for span and return a string that is including the word star

def StarLocator(item):
    numberOfStars=''
    stars = item.find_elements_by_tag_name('span')
    for items in stars:
        innerHtml = items.get_attribute('innerHTML')
        if innerHtml.find("star", 0, 20) != -1:
            return  innerHtml
            break
    return ''