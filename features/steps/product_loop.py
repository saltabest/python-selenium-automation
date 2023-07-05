from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name")
CURRENT_COLOR = (By.CSS_SELECTOR, 'span.a-button-inner')


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