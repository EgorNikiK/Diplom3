from pages.base_page import BasePage
from helpers.urls import Urls


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Urls.HOME_PAGE_URL)
