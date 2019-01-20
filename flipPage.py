from myimports import *

#simple mathud to flip the page, will destingush between the div vertion and the li version of amazon search results

def FlipPage(browser,timeout):
    try:
        element_present = EC.presence_of_element_located((By.ID, 'pagnNextString'))
        WebDriverWait(browser, timeout).until(element_present)
        element = browser.find_element_by_id('pagnNextString').click()
    except TimeoutException:
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'li.a-last'))
            WebDriverWait(browser, timeout).until(element_present)
            elements = browser.find_elements_by_css_selector('li.a-last')
            for element in elements:
                text=element.get_attribute('innerHTML')
                if text.find('Next')>-1:
                    element.click()
                    break
        except TimeoutException:
            print('Timed out waiting for page to load')
    return True