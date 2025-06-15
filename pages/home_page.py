from pages.base_page import BasePage
from helpers.locators import HomePageLocators
from helpers.urls import Urls

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Urls.HOME_PAGE_URL)

    def click_constructor_button(self):
        self.click_on_element(HomePageLocators.constructor_button)

    def click_order_feed_button(self):
        self.click_on_element(HomePageLocators.order_feed_button)

    def click_ingredient(self):
        self.click_on_element(HomePageLocators.Bun_ingredient)

    def exit_ingredient_card(self):
        self.click_on_element(HomePageLocators.exit_ingredient_button)

    def drag_and_drop_ingredient(self, ingredient_locator, basket_locator):
        self.drag_and_drop_element(self.driver, ingredient_locator, basket_locator)