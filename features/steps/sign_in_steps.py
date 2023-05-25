from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open Amazon Page")
def open_amazon(context):
    context.driver.get("https://www.amazon.com")


@when("Click Orders")
def click_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/css/order-history?ref_=nav_orders_first"]').click()


@then("Verify Sign In header is visible")
def sign_in_header(context):
    context.driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]')


@then("Verify email input field is present")
def email_field(context):
    context.driver.find_element(By.CSS_SELECTOR, '#ap_email')
    expected_text = "Sign In"
    actual_text = context.driver.find_element(By.ID, "ap_email")
    assert actual_text == expected_text, f"expected {expected_text}, but got {actual_text}"


