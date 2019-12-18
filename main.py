from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


config = configparser.ConfigParser()
config.read('.config')
driver = webdriver.Chrome('/usr/bin/google-chrome',
                          chrome_options=chrome_options)

# Access Site
try:
    driver.get('http://www.1point3acres.com/bbs/')
except:
    print('Could not access http://www.1point3acres.com/bbs/')

# Login
try:
    driver.find_element_by_id("ls_username").send_keys(
        config['DEFAULT']['USERNAME'])
    driver.find_element_by_id("ls_password").send_keys(
        config['DEFAULT']['PASSWORD'])
    time.sleep(config['DEFAULT']['SLEEPTIME'])
    driver.find_element_by_css_selector("button.pn.vm").click()
    time.sleep(config['DEFAULT']['SLEEPTIME'])
except:
    print('Couldn\'t login')

# Click Daily Reward
try:
    driver.find_element_by_xpath("//div[@id='um']/p[2]/a[3]/font").click()
    time.sleep(config['DEFAULT']['SLEEPTIME'])
except:
    print('Couldn\'t access daily reward')

# Choose Sentiment
try:
    driver.find_element_by_css_selector("#fd > center > img").click()
    time.sleep(config['DEFAULT']['SLEEPTIME'])
except:
    print('Sentiment not found')

# Autofill review
try:
    driver.find_element_by_xpath("(//input[@name='qdmode'])[2]").click()
    time.sleep(config['DEFAULT']['SLEEPTIME'])
except:
    print('Autofill review fail')

# Submit daily request
try:
    driver.find_element_by_css_selector("button.pn.pnc").click()
except:
    print('Submit daily request fail')

# Quit
driver.quit()
