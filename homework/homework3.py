from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)

driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.find_element(By.ID. 'createAccountSubmit').click()
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name' )
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR,'input[name="metadata1"]')
driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_condition_of_use"]')
driver.find_element(By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496"]')
driver.find_element(By.CSS_SELECTOR, 'a[class="a-link-emphasis"]')
driver.find_element(By.CSS_SELECTOR,'a#ab-registration-link')


