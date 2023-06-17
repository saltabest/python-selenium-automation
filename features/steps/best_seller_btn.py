from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@when("Click on Best Sellers")
def best_seller_btn(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href,'ref_=nav_cs_bestsellers')]").click()




@then("Verify 5 Links")
def verify_5_links(context):
    expected_result = 5
    actual_result = context.driver.find_elements(By.CSS_SELECTOR, "#zg_header a")
    assert len(actual_result) == expected_result, f"expected {expected_result}, but got {actual_result}"
