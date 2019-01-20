from myimports import *

#mathud to return the price of the item

def PriceLocator(item):
    findPrice = item.find_elements_by_css_selector("span.a-offscreen")
    for items in findPrice:
        innerHtml = items.get_attribute('innerHTML')
        if innerHtml.find("$") != -1:
            return  innerHtml
            break
    return ''