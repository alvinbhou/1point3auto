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
SLEEP_TIME = 4

# Access Site
try:
    driver.get('http://www.1point3acres.com/bbs/')
    print('Successful Access Site')
except BaseException:
    print('Could not access http://www.1point3acres.com/bbs/')
    exit(1001)

# Login
try:
    driver.find_element_by_id("ls_username").send_keys(
        os.environ.get("USERNAME"))
    driver.find_element_by_id("ls_password").send_keys(
        os.environ.get("PASSWORD"))
    time.sleep(SLEEP_TIME)
    driver.find_element_by_css_selector("button.pn.vm").click()
    print('Successful Login')
    time.sleep(SLEEP_TIME)
except BaseException:
    print('Couldn\'t login')
    exit(1002)

# Click Daily Reward
try:
    driver.find_element_by_xpath("//font[text()='签到领奖!']").click()
    time.sleep(SLEEP_TIME)
    print('Successful click Daily Reward')
except Exception as e:
    print(e)
    print('Couldn\'t access daily reward')
    exit(1003)

# Choose Sentiment
try:
    driver.find_element_by_css_selector("#fd > center > img").click()
    time.sleep(SLEEP_TIME)
    print('Successful Choose Sentiment')
except BaseException:
    print('Sentiment not found')
    exit(1004)

# Autofill Review
try:
    driver.find_element_by_xpath("(//input[@name='qdmode'])[2]").click()
    print('Successful Autofill review')
    time.sleep(SLEEP_TIME)
except BaseException:
    print('Autofill review fail')
    exit(1005)

# Submit daily request
try:
    driver.find_element_by_css_selector("button.pn.pnc").click()
    print('Successful Submit daily request')
except BaseException:
    print('Submit daily request fail')
    exit(1006)

# Quit
driver.quit()
exit(0)
