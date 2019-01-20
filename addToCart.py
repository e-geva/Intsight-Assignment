from myimports import *
from listLocator import ListLocator

def AddToCart(browser,timeout):
    items=ListLocator(browser,timeout)
    name=''
    for item in items:
        try:
            element_present = EC.presence_of_element_located((By.TAG_NAME, 'h2'))
            WebDriverWait(browser, timeout).until(element_present)
            elements = item.find_elements_by_tag_name('h2')
            if len(elements)==0:
                elements = item.find_elements_by_tag_name('h5')
            for element in elements:
                name=element.text
                element.click()
                browser.implicitly_wait(3)
                element_present2 = EC.presence_of_element_located((By.ID, 'add-to-cart-button'))
                WebDriverWait(browser, timeout).until(element_present2)
                element2 = browser.find_element_by_id('add-to-cart-button').click()
                element_present3 = EC.presence_of_element_located((By.ID, 'nav-cart'))
                WebDriverWait(browser, timeout).until(element_present3)
                element3 = browser.find_element_by_id('nav-cart').click()
                element_present4 = EC.presence_of_element_located((By.ID, 'activeCartViewForm'))
                WebDriverWait(browser, timeout).until(element_present4)
                element4 = browser.find_element_by_id('activeCartViewForm')
                text=element4.get_attribute('innerHTML')
                if text.find(name)!=-1:
                    print('Found it')
                    return True
                else:
                    print('Didnt find it')
                    return False
        except TimeoutException:
            print('Timed out waiting for page to load')
