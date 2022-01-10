from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome, edge

edge_driver = "drivers/msedgedriver.exe"

# check if edge_driver exist
import os

if not os.path.exists("drivers/msedgedriver.exe"):
    raise FileNotFoundError("""
        Microsoft Edge WebDriver not found.
        Please download WebDriver Here: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        Required FilePath: drivers/msedgedriver.exe
    """)

url = 'https://www.bing.com'


if __name__ == '__main__':
    edge_options = edge.options.Options()
    edge_options._binary_location = "C:/Program Files (x86)/Microsoft\Edge/Application/msedge.exe"
    edge_options.add_argument('--disable-blink-features=AutomationControlled')  # thanks @soumil-shah
    edge_options.add_argument('--disable-blink-features=AutomationControlled')  # thanks @soumil-shah
    edge_options.add_experimental_option("useAutomationExtension", False)
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Edge(executable_path=edge_driver, options=edge_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  # thanks @soumil-shah
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })  # thanks @soumil-shah

    driver.get(url)

    from data.searches import common_search_terms
    from random import uniform, choice
    from time import sleep


    for i in range(30):
        sleep(uniform(1.7, 4))
        elm_search_box = driver.find_element(value="sb_form_q")
        elm_search_box.clear()
        sleep(uniform(0.5, 2))
        elm_search_box.send_keys(choice(common_search_terms))
        sleep(uniform(0.3, 0.9))
        elm_search_box.send_keys(Keys.ENTER)
        sleep(uniform(6, 10.5))

    driver.quit()
