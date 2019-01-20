from myimports import *

#Mathod to enter the requested key and search the site

def Searcher(browser,timeout,key):
    try:
        element_present = EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
        WebDriverWait(browser, timeout).until(element_present)
        element = browser.find_element_by_id('twotabsearchtextbox')
        element.send_keys(key)
    except TimeoutException:
        print('Timed out waiting for page to load')
    try:
        element_present = EC.presence_of_element_located((By.ID, 'nav-search-submit-text'))
        WebDriverWait(browser, timeout).until(element_present)
        browser.find_element_by_class_name('nav-input').click()
    except TimeoutException:
        print('Timed out waiting for page to load')
    return True