from selenium.webdriver.common.by import By
from .base_page import BasePage
import re
from features.screenshots.conftest import shared_data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage(BasePage):
    cart_items = (By.XPATH, "//div[@class='cPHDOP col-12-12']/div[@class='eGXlor pk3Guc']")
    total_price = (By.XPATH, "//div[@class='PWd9A7']//div[@class='PWd9A7 xvz6eC']/div[2]")#"//div[text()='Total Amount']/../..//div[@class='PWd9A7 xvz6eC']/div[2]")#"//div[text()='Total Amount']/../..//span[contains(text(),'₹')]")
    remove_button_samsung = (By.XPATH, "//a[contains(@href,'samsung')]/../following-sibling::div//div[text()='Remove']")
    remove_button_pop_up = (By.XPATH, "//div[@class='gRTtwM f-DWwy']/div[text()='Remove']")
    price_of_items = (By.XPATH, "//div[@class='cPHDOP col-12-12']/div[@class='eGXlor pk3Guc']//span[@class='LAlF6k re6bBo']")
    success_msg = (By.XPATH, "//div[contains(text(),'Successfully removed ')]")
    number_of_items_flipkart = (By.XPATH, "//div[text()='Flipkart (1)']")

    def verify_items_in_cart(self, expected_items):
        self.wait_for_element((By.XPATH, "//div[@class='cPHDOP col-12-12']/div[@class='eGXlor pk3Guc']"))
        items = self.driver.find_elements(*self.cart_items)
        print('Items are----'+str(len(items)))
        print('expected_items Items are----'+str(expected_items))
        assert len(items) == int(expected_items)
        
    def fetch_total_price_original(self, shared_data):
        total = self.driver.find_element(*self.total_price).text
        print('Total price '+str(total))
        total_price_actual = re.sub(r'\D', '', total)
        print('Total price Original '+str(total_price_actual))
        return total_price_actual
        # shared_data['total_price_original']=total_price_actual

    def verify_total_price(self, expected_price, shared_data):
        # total = self.driver.find_element(*self.total_price).text
        # print('Total price '+str(total))
        # total_price_actual = re.sub(r'\D', '', total)
        print('Total price Actual '+str(expected_price))
        # import time
        # time.sleep(80)
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.price_of_items))
        # Find the elements
        cart_items_price = self.driver.find_elements(*self.price_of_items)
        print('cart_items_price list'+str(cart_items_price))
        total_price_expected = 0
        # Iterate through the list of prices
        for item in cart_items_price:
            price_string = item.text  # Get the text of the price element
            print('price_string '+str(price_string))
            # Use regular expression to extract numerical value
            numerical_value = re.sub(r'\D', '', price_string)
            shared_data['to_be_removed_item_price'] = numerical_value
            # Convert the numerical value to an integer and add to total price
            if numerical_value:
                total_price_expected += int(numerical_value)
        print('total_price_expected '+str(total_price_expected))
        print('to_be_removed_item_price '+str(shared_data['to_be_removed_item_price'] ))
        assert int(expected_price) == int(total_price_expected)

    def remove_item(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(self.remove_button_samsung))
        self.driver.find_element(*self.remove_button_samsung).click()
        self.wait_for_element(self.remove_button_pop_up)
        self.driver.find_element(*self.remove_button_pop_up).click()
        self.wait_for_element(self.success_msg)
        self.wait_for_element(self.number_of_items_flipkart)
