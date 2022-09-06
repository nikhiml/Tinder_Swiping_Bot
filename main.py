from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

import time

email = '*************'
pwd = '*******'
url = '************'

chrome_driver_path = '/Users/nikhilmittal/Documents/Selenium/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)

time.sleep(10)

log_in = driver.find_element(by=By.XPATH, value='//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()
time.sleep(5)

try:
    fb_log_in = driver.find_element(by=By.XPATH,
                                    value='//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    fb_log_in.click()

except NoSuchElementException:
    more_options = driver.find_element(by=By.XPATH,
                                       value='// *[ @ id = "s18585620"] / div / div / div[1] / div / div / div[3] / span / button')
    more_options.click()
    time.sleep(5)
    fb_log_in = driver.find_element(by=By.XPATH,
                                    value='//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    fb_log_in.click()

driver.switch_to.window(driver.window_handles[1])
user_email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
user_email.send_keys(email)
user_pwd = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
user_pwd.send_keys(pwd)
log_in = driver.find_element(by=By.CSS_SELECTOR, value='#loginform #loginbutton input')
log_in.click()

driver.switch_to.window(driver.window_handles[0])

time.sleep(15)

allow_btn = driver.find_element(by=By.XPATH, value='//*[@id="s18585620"]/div/div/div/div/div[3]/button[1]/span')
allow_btn.click()

time.sleep(2)

enable_btn = driver.find_element(by=By.XPATH, value='//*[@id="s18585620"]/div/div/div/div/div[3]/button[1]/span')
enable_btn.click()

time.sleep(2)

cookies_yes = driver.find_element(by=By.XPATH, value='//*[@id="s1746966696"]/div/div[2]/div/div/div[1]/div[1]/button/span')
cookies_yes.click()

time.sleep(5)

n = 0
for n in range(10):
    try:
        btns = driver.find_elements(by=By.CSS_SELECTOR, value='.Isolate button')
    except NoSuchElementException:
        time.sleep(2)
        btns = driver.find_elements(by=By.CSS_SELECTOR, value='.Isolate button')
    finally:
        for btn in btns:
            if btn.get_attribute('data-testid') == 'gamepadLike':
                try:
                    btn.click()
                except ElementClickInterceptedException:
                    not_interest = driver.find_element(by=By.XPATH,
                                                       value='//*[@id="s18585620"]/div/div/div[2]/button[2]/span')
                    not_interest.click()
                    btn.click()

    time.sleep(3)

print(f'{n+1} people liked')

driver.quit()
