from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get(
    "CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Test usage of selenium
SLEEP_TIME = 2

# Access Site
try:
    driver.get('http://www.1point3acres.com/bbs/')
except:
    print('Could not access http://www.1point3acres.com/bbs/')

# Login
try:
    driver.find_element_by_id("ls_username").send_keys(
        os.environ.get("USERNAME"))
    driver.find_element_by_id("ls_password").send_keys(
        os.environ.get("PASSWORD"))
    time.sleep(SLEEP_TIME)
    driver.find_element_by_css_selector("button.pn.vm").click()
    time.sleep(SLEEP_TIME)
except:
    print('Couldn\'t login')

# Click Daily Reward
try:
    driver.find_element_by_xpath("//div[@id='um']/p[2]/a[3]/font").click()
    time.sleep(SLEEP_TIME)
except:
    print('Couldn\'t access daily reward')

# Choose Sentiment
try:
    driver.find_element_by_css_selector("#fd > center > img").click()
    time.sleep(SLEEP_TIME)
except:
    print('Sentiment not found')

# Autofill review
try:
    driver.find_element_by_xpath("(//input[@name='qdmode'])[2]").click()
    time.sleep(SLEEP_TIME)
except:
    print('Autofill review fail')

# Submit daily request
try:
    driver.find_element_by_css_selector("button.pn.pnc").click()
except:
    print('Submit daily request fail')

# Quit
driver.quit()
