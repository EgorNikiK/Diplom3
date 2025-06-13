import allure
import time
from helpers.locators import PersonalAccountPageLocators
from helpers.urls import Urls
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на кнопку Личный кабинет и переходим на страницу авторизации.')
    def click_on_personal_account_button(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.personal_account_button)
        self.click_on_element(PersonalAccountPageLocators.personal_account_button)
        self.wait_visibility_of_element(PersonalAccountPageLocators.entrance_label)

    @allure.step('Авторизуемся в личном кабинете с помощью логина и пароля.')
    def do_login(self, email, password):
        self.wait_clickability_of_element(PersonalAccountPageLocators.personal_account_button)
        self.click_on_element(PersonalAccountPageLocators.personal_account_button)
        self.wait_visibility_of_element(PersonalAccountPageLocators.entrance_label)
        self.find_element_on_page(PersonalAccountPageLocators.email_field).send_keys(email)
        self.find_element_on_page(PersonalAccountPageLocators.password_field).send_keys(password)
        self.click_on_element(PersonalAccountPageLocators.entrance_button)

    @allure.step('Нажимаем на кнопку Личный кабинет и переходим на страницу Профиль пользователя.')
    def go_to_user_profile_page(self):
        self.wait_clickability_of_element(PersonalAccountPageLocators.personal_account_button)
        self.click_on_element(PersonalAccountPageLocators.personal_account_button)
        self.wait_visibility_of_element(PersonalAccountPageLocators.order_history_button)

    @allure.step('Входим в личный кабинет пользователя.')
    def enter_to_personal_account(self, email, password):
        self.open_url(Urls.HOME_PAGE_URL)
        self.do_login(email, password)
        time.sleep(1)
        self.go_to_user_profile_page()

    @allure.step('Переходим в раздел История заказов.')
    def go_to_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.order_history_button)
        time.sleep(1)
        self.check_element_is_focused(PersonalAccountPageLocators.order_history_button)

    @allure.step('Выходим из личного кабинета.')
    def do_logout(self):
        self.click_on_element(PersonalAccountPageLocators.exit_button)
        self.wait_visibility_of_element(PersonalAccountPageLocators.entrance_label)
