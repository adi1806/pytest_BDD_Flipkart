import pytest
from pytest_bdd import scenarios, given, when, then
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage
from features.pages.item_page import ItemPage
from features.pages.cart_page import CartPage
from features.utils.test_data import test_data
from features.screenshots.conftest import shared_data
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


featureFileDir = 'features'
featureFile = 'item_ordering.feature'
BASE_DIR = Path(__file__).resolve().parent.parent
FEATURE_FILE = BASE_DIR.joinpath(featureFile)
print(FEATURE_FILE)

scenarios(FEATURE_FILE)

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@given('I open Flipkart')
def open_flipkart(browser):
    browser.get(test_data['url'])

@when('I search for "Samsung S24 128 GB" and select the second item')
def search_and_select_samsung(browser):
    home_page = HomePage(browser)
    home_page.search_item(test_data['items'][0])
    search_results_page = SearchResultsPage(browser)
    search_results_page.select_second_item()

@when('I check the item\'s availability and add it to the cart')
def check_availability_and_add(browser):
    item_page = ItemPage(browser)
    item_page.check_availability_and_add_to_cart(test_data['pin_code'])

@when('I return to the home page')
def return_home(browser):
    item_page = ItemPage(browser)
    item_page.navigate_to_home_page()

@when('I search for "bajaj iron majesty" and select the second item')
def search_and_select_bajaj(browser):
    home_page = HomePage(browser)
    home_page.search_item(test_data['items'][1])
    search_results_page = SearchResultsPage(browser)
    search_results_page.select_second_item()

@then('I navigate to the cart')
def navigate_to_cart(browser):
    browser.get(test_data['url_cart'])

@then('I verify both items are present in the cart')
def verify_items_in_cart(browser, shared_data):
    cart_page = CartPage(browser)
    cart_items = cart_page.verify_items_in_cart()
    assert len(cart_items) == 2
    total_price_original = cart_page.fetch_total_price_original()
    shared_data['total_price_original']=total_price_original

@then('I verify the total price reflects the sum of both items')
def verify_total_price(browser, shared_data):
    cart_page = CartPage(browser)
    # Assuming you have a way to calculate the expected price
    expected_original_price = shared_data['total_price_original']
    print('expected_original_price '+expected_original_price)
    total_price_summation = cart_page.verify_total_price(shared_data)
    assert int(total_price_summation) == int(expected_original_price)

@when('I remove one item from the cart')
def remove_item_from_cart(browser):
    cart_page = CartPage(browser)
    cart_page.remove_item()

@then('I confirm the total price is updated accordingly')
def confirm_total_price_update(browser, shared_data):
    cart_page = CartPage(browser)
    # Assuming you have a way to calculate the updated price
    expected_price = int(shared_data['total_price_original'])-int(shared_data['to_be_removed_item_price'])
    print('Updated price '+str(expected_price))
    cart_page.verify_total_price(shared_data)
