from selenium.webdriver.common.by import By
from .base_page import BasePage
import re
# from features.screenshots.conftest import shared_data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage(BasePage):
    cart_items = (By.XPATH, "//div[@class='cPHDOP col-12-12']/div[@class='eGXlor pk3Guc']")
    total_price = (By.XPATH, "//div[@class='PWd9A7']//div[@class='PWd9A7 xvz6eC']/div[2]")
    remove_button_last = (By.XPATH, "(//a[contains(@href,'marketplace=FLIPKART')]/../following-sibling::div//div[text()='Remove'])[last()]")
    remove_button_pop_up = (By.XPATH, "//div[@class='gRTtwM f-DWwy']/div[text()='Remove']")
    price_of_items = (By.XPATH, "//div[@class='cPHDOP col-12-12']/div[@class='eGXlor pk3Guc']//span[@class='LAlF6k re6bBo']")
    success_msg = (By.XPATH, "//div[contains(text(),'Successfully removed ')]")
    number_of_items_flipkart = (By.XPATH, "//div[text()='Flipkart (1)']")

    def verify_items_in_cart(self):
        self.wait_for_element((By.XPATH, "//div[@class='cPHDOP col-12-12']/div[@class='eGXlor pk3Guc']"))
        cart_items = self.driver.find_elements(*self.cart_items)
        print('cart_items are----'+str(len(cart_items)))
        return cart_items
        
    def fetch_total_price_original(self):
        total = self.driver.find_element(*self.total_price).text
        total_price_original = re.sub(r'\D', '', total)
        print('Total price Original '+str(total_price_original))
        return total_price_original

    def verify_total_price(self, shared_data):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.price_of_items))
        # Find the elements
        cart_items_price = self.driver.find_elements(*self.price_of_items)
        print('cart_items_price list'+str(cart_items_price))
        total_price_summation = 0
        # Iterate through the list of prices
        for item in cart_items_price:
            price_string = item.text  # Get the text of the price element
            print('price of each item '+str(price_string))
            # Use regular expression to extract numerical value
            numerical_value = re.sub(r'\D', '', price_string)
            if int(numerical_value)!=0:
                shared_data['to_be_removed_item_price'] = numerical_value
            # Convert the numerical value to an integer and add to total price
            if numerical_value:
                total_price_summation += int(numerical_value)
        print('total_price_summation '+str(total_price_summation))
        print('to_be_removed_item_price '+str(shared_data['to_be_removed_item_price']))
        return total_price_summation

    def remove_item(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.remove_button_last).click()
        self.wait_for_element(self.remove_button_pop_up)
        self.driver.find_element(*self.remove_button_pop_up).click()
        self.wait_for_element(self.success_msg)
        self.wait_for_element(self.number_of_items_flipkart)
