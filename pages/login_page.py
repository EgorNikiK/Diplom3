from pages.base_page import BasePage
from helpers.locators import LoginPageLocators
from helpers.urls import Urls

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Urls.LOGIN_PAGE_URL)

    def click_recovery_password_button(self):
        self.click_on_element(LoginPageLocators.recovery_password_button)
