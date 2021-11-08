from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def go_to_waketech():
    driver = webdriver.Chrome()
    driver.get('https://en.wikipedia.org')
    search = driver.find_element(By.ID, 'searchInput')
    search.send_keys("wake tech")
    time.sleep(2)
    search.send_keys(Keys.RETURN)

    title = driver.find_element(By.XPATH, '//title').get_attribute("innerHTML")
    return title

go_to_waketech()

