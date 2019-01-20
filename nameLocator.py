from myimports import *

#mathud that will return the name of the item and the author of the item

def NameLocator(item):
    links_list = item.find_elements_by_css_selector("a.a-link-normal")
    name,author = '',''
    counter = 0
    for link in links_list:
        text = link.text
        if text != '':
            if counter == 0:
                name = text
            if counter == 1:
                author = text
            counter = counter + 1
    return name,author