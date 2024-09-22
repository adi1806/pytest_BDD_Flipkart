from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        for _ in range(3):  # Retry up to 3 times
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                break  # Exit loop if successful
            except StaleElementReferenceException:
                continue  # Retry if exception occurs

    def click_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        for _ in range(3):  # Retry up to 3 times
            try:
                element = wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element = wait.until(EC.visibility_of_element_located(locator))
                element.click()
                break  # Exit loop if successful
            except StaleElementReferenceException:
                continue  # Retry if exception occurs
            except ElementClickInterceptedException:
                continue
