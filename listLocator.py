from myimports import *

#simple mathud to return a list of items, will destingush between the div vertion and the li version of amazon search results

def ListLocator(browser,timeout):
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.s-result-list'))
        WebDriverWait(browser, timeout).until(element_present)
        html_list = browser.find_element_by_css_selector("div.s-result-list")
        items = html_list.find_elements_by_css_selector("div.s-result-item")
        return items

    except (NoSuchElementException, TimeoutException):
        html_list = browser.find_element_by_tag_name("ul")
        items = html_list.find_elements_by_tag_name("li")
        return items