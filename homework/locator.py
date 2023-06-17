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


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@given("Open product page B079KCTN1D")
def open_page(context):
    context.driver.get("https://www.amazon.com/dp/B079KCTN1D")


@then("Verify user can click on different options")
def verify_can_click_colors(context):
    expected_result = ["Blue Jay", "Peacock Blue", "Plum"]
    actual_resul = []
    colors = context.driver.find_element(*COLOR_OPTIONS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [*CURRENT_COLOR]

    assert expected_colors == actual_colors, \
       f'Expected colors {expected_colors} did not match actual {actual_colors}'


