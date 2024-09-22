from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ItemPage(BasePage):
    pin_code_box = (By.ID, 'pincodeInputId')
    check_button = (By.XPATH, "//span[text()='Check']")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    flipkart_home_page = (By.XPATH, "//a/img[@title='Flipkart']")
    close_btn = (By.XPATH, "//span[@role='button']")

    def check_availability_and_add_to_cart(self, pin_code):
        self.wait_for_element((self.pin_code_box))
        self.driver.find_element(*self.pin_code_box).send_keys(pin_code)
        self.driver.find_element(*self.check_button).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_for_element((self.add_to_cart_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH, "//button[text()='Add to cart']"))
        # import time
        # time.sleep(5)
        # self.driver.execute_script("window.scrollTo({ top: 1500, behavior: 'smooth' });")
        # self.driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        # self.driver.execute_script("window.scrollTo(0, 4000);")
        # self.driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        self.click_element(self.add_to_cart_button)
    
    def navigate_to_home_page(self):
        self.driver.find_element(*self.flipkart_home_page).click()
        self.wait_for_element((self.close_btn))
        self.driver.find_element(*self.close_btn).click()
        
