from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    search_box = (By.NAME, 'q')
    search_button = (By.XPATH, "//button[@type='submit']")

    def search_item(self, item_name):
        self.wait_for_element(self.search_box)
        self.driver.find_element(By.NAME, 'q').send_keys(item_name)
        self.wait_for_element(self.search_button)
        # self.driver.find_element(*self.search_button).click()
        self.click_element(self.search_button)
