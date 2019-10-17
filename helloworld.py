from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@title="Babbelbox 😁"]'))
    )
finally:
    print('Loaded!')
    element = driver.find_element_by_xpath('//*[@title="Babbelbox 😁"]')
    element.click()
    element = driver.find_element_by_class_name("_3u328")
    element.send_keys("Dit is een robotje. Hallo wereld!")
