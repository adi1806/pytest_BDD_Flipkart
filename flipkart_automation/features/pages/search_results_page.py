from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    search_items = (By.XPATH, "//div[contains(@class, 'DOjaWF')][2]/div[contains(@class,'cPHDOP col-12-12')]//div[@data-id]")
    def select_second_item(self):
        items = self.driver.find_elements(*self.search_items)
        # Ensure there are at least two items
        if len(items) > 1:
            self.wait_for_element((By.XPATH, "//div[contains(@class, 'DOjaWF')][2]/div[contains(@class,'cPHDOP col-12-12')]//div[@data-id]"))
            # Scroll the element into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", items[1])
            items[1].click()
            # Switch to new window
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
        else:
            print("Less than two items found")

