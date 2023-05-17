from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID, 'ap-other-signin-issues-link')
driver.find_element(By.ID, 'createAccountSubmit')
driver.find_element(By.XPATH, '//a[contains(@href, "ap_signin_notification_privacy_notice")]')
driver.find_element(By.XPATH, '//a[contains(@href, "ap_signin_notification_condition_of_use")]')
driver.find_element(By.ID,"auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")


