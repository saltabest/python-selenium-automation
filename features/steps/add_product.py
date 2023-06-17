from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

search_word = (By.CSS_SELECTOR, "#titleSection")
price= (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
add_btn=(By.CSS_SELECTOR, '#add-to-cart-button')
prod_title = (By.CSS_SELECTOR, ".a-truncate-cut")

@when("Input {product} into search")
def toy(context, product):

    search = context.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    search.clear()
    search.send_keys(product)





@when("Click on search")
def search(context):
       context.driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()
       context.driver.wait.until()




@when("Add first product")
def add_first_product(context):
    context.driver.find_element(*price).click()

    context.product_name = context.driver.find_element(*search_word).text


@when("Click add to cart")
def add_to_cart(context):
    context.driver.find_element(*add_btn).click()




@when("Navigate to cart")
def go_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "#nav-cart"))
    context.driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()



@then("Verify cart has right product")
def verify_right_name(context):
    actual_name = context.driver.find_element(*prod_title).text
    assert context.product_name[:30] in actual_name, f"Expected {context.product_name} but got {actual_name}"