from behave import given, when, then

from pages.category_page import CategoryPage
from pages.checkout_page import CheckoutPage
from pages.completed_page import CompletedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.shopping_cart import ShoppingCartPage


@given('I open the main page')
def step_impl(context):
    context.main_page = MainPage(context.driver, context.base_url, context.logger)
    context.main_page.navigate_to_main_page()
    assert context.main_page.check_page_is_opened()


@when('I click "Log in" link in the header')
def step_impl(context):
    context.main_page.click_login()
    context.login_page = LoginPage(context.driver, context.base_url, context.logger)
    assert context.login_page.check_page_is_opened()


@when('I enter valid credentials for an existing user')
def step_impl(context):
    context.login_page.enter_email("ValMor@gmail.com")
    context.login_page.enter_password("passw0rd")


@when('I click "Log in" button')
def step_impl(context):
    context.login_page.click_login_button()
    assert context.main_page.check_page_is_opened()


@then('I should be logged in successfully')
def step_impl(context):
    assert context.main_page.check_logged_in()


@when('I enter "{search_text}" in the search panel')
def step_impl(context, search_text):
    context.main_page.enter_search_term(search_text)


@when('I click "Search" button on the main page')
def step_impl(context):
    context.main_page.click_search()
    context.search_page = SearchPage(context.driver, context.base_url, context.logger)
    assert context.search_page.check_page_is_opened()


@then('There should be {number} products displayed on the search page')
def step_impl(context, number):
    assert context.search_page.check_number_of_products(number)


@when('I open "Advanced Search"')
def step_impl(context):
    context.search_page.open_advanced_search()
    assert context.search_page.check_advanced_search_is_opened()


@when('I select "{category}" from the "Category" dropdown')
def step_impl(context, category):
    context.search_page.select_category(category)


@when('I set the "Price range" to From {price_from} to {price_to}')
def step_impl(context, price_from, price_to):
    context.search_page.set_price_range(price_from, price_to)


@when('I click "Search" button on the search page')
def step_impl(context):
    context.search_page.click_search_button()
    assert context.search_page.check_page_is_opened()


@then('The first product in the search should have the title "{product_title}"')
def step_impl(context, product_title):
    assert context.search_page.check_first_product_title(product_title)


@when('I navigate to the "{category}" category from the top menu')
def step_impl(context, category):
    context.main_page.navigate_to_category_from_top_menu(category)
    context.category_page = CategoryPage(context.driver, context.base_url, context.logger)
    assert context.category_page.check_category_page_is_opened(category)


@when('I select the "{subcategory_name}" subcategory')
def step_impl(context, subcategory_name):
    context.category_page.open_subcategory(subcategory_name)
    context.category_page = CategoryPage(context.driver, context.base_url, context.logger)
    assert context.category_page.check_category_page_is_opened(subcategory_name)


@when('I open the "{product}" product page')
def step_impl(context, product):
    context.category_page.open_product(product)
    context.product_page = ProductPage(context.driver, context.base_url, context.logger)
    assert context.product_page.check_product_page_is_opened(product)


@when('I click "Add to cart" button')
def step_impl(context):
    context.product_page.add_product_to_cart()


@then('A success notification bar should be visible in the header')
def step_impl(context):
    assert context.product_page.check_success_bar_notification()


@then('The shopping cart should contain {number} products')
def step_impl(context, number):
    assert context.main_page.check_shopping_cart_number_of_products(number)


@when('I open the shopping cart from the link in the header')
def step_impl(context):
    context.main_page.navigate_to_shopping_cart()
    context.shopping_cart_page = ShoppingCartPage(context.driver, context.base_url, context.logger)
    assert context.shopping_cart_page.check_page_is_opened()


@when('I agree with terms of service by clicking the checkbox')
def step_impl(context):
    context.shopping_cart_page.agree_with_terms_of_service()


@when('I click "Checkout" button')
def step_impl(context):
    context.shopping_cart_page.navigate_to_checkout()
    context.checkout_page = CheckoutPage(context.driver, context.base_url, context.logger)
    assert context.checkout_page.check_page_is_opened()


@when('I click "Continue" in the Billing Address block')
def step_impl(context):
    context.checkout_page.click_button_in_block("billing_address")


@when('I click "Continue" in the Shipping Address block')
def step_impl(context):
    context.checkout_page.click_button_in_block("shipping_address")


@when('I click "Continue" in the Shipping Method block')
def step_impl(context):
    context.checkout_page.click_button_in_block("shipping_method")


@when('I click "Continue" in the Payment Method block')
def step_impl(context):
    context.checkout_page.click_button_in_block("payment_method")


@when('I click "Continue" in the Payment Information block')
def step_impl(context):
    context.checkout_page.click_button_in_block("payment_info")


@when('I click "Confirm" in the Confirm Order block')
def step_impl(context):
    context.checkout_page.click_button_in_block("confirm")
    context.completed_page = CompletedPage(context.driver, context.base_url, context.logger)
    assert context.completed_page.check_page_is_opened()


@then('The completed message should contain the correct text')
def step_impl(context):
    assert context.completed_page.check_success_message()
