import allure
import time
from helpers.locators import HomePageLocators, PersonalAccountPageLocators, OrderFeedPageLocators
from helpers.urls import Urls
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderFeedPage(PersonalAccountPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Urls.ORDER_FEED_URL)

    @allure.step('Нажимаем на заказ, получаем открытое окно с заказом.')
    def get_order_details_by_clicking_on_order_in_feed(self, locator):
        self.wait_visibility_of_element(locator)
        self.scroll_to_element(locator)
        self.click_on_element(locator)
        return self.wait_visibility_of_element(OrderFeedPageLocators.order_card_label)

    @allure.step('Находим на странице заказ и нажимаем на него.')
    def find_order_from_personal_account_in_order_feed(self):
        self.find_element_on_page(PersonalAccountPageLocators.order_in_account)
        order_id_in_account = self.get_element_text(PersonalAccountPageLocators.order_in_account)
        self.click_on_element(HomePageLocators.order_feed_button)
        time.sleep(1)
        locator = (By.XPATH, f".//p[text()='{order_id_in_account}']")
        order_in_feed = self.find_element_on_page(locator)
        return order_in_feed

    @allure.step('Ожидаем отображение номера заказа в разделе В работе')
    def wait_order_number_in_working_order_list(self, number):
        return (WebDriverWait(self.driver, 10).
                until(expected_conditions.text_to_be_present_in_element(OrderFeedPageLocators.order_in_work, number)))
