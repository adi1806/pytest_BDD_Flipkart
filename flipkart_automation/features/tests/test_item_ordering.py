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
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

featureFileDir = 'features'
featureFile = 'item_ordering.feature'
BASE_DIR = Path(__file__).resolve().parent.parent
FEATURE_FILE = BASE_DIR.joinpath(featureFile)
print(FEATURE_FILE)

# @scenarios('../flipkart_automation/features/item_ordering.feature')
# @scenarios('C:/Users/ac57486/OneDrive - Lumen/Pictures/MyFolder/BDD/flipkart_automation/features/item_ordering.feature')
# @scenario(FEATURE_FILE, 'Order items and verify cart')

scenarios(FEATURE_FILE)
# def test_publish():
#     pass

        
# @pytest.fixture
# def open_browser():
#     print('Inside')
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

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

@when('I search for "Samsung S22 128 GB" and select the second item')
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
    # browser.get('https://www.flipkart.com')
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
    cart_page.verify_items_in_cart(2)
    total_price_actual = cart_page.fetch_total_price_original(shared_data)
    shared_data['total_price_original']=total_price_actual

@then('I verify the total price reflects the sum of both items')
def verify_total_price(browser, shared_data):
    cart_page = CartPage(browser)
    # Assuming you have a way to calculate the expected price
    expected_price = shared_data['total_price_original']
    print('First time price '+expected_price)
    cart_page.verify_total_price(expected_price, shared_data)

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
    cart_page.verify_total_price(expected_price, shared_data)
