from selenium import webdriver
from selenium.webdriver.common.keys import Keys

edge_driver = "drivers/msedgedriver.exe"
url = 'https://www.bing.com'

if __name__ == '__main__':
    driver = webdriver.Edge(edge_driver)
    driver.get(url)

    elm_search_box = driver.find_element(value="sb_form_q")
    elm_search_box.send_keys("some keys")
    elm_search_box.send_keys(Keys.ENTER)
