import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from helpers.urls import Urls
from helpers.locators import HomePageLocators

class TestBasicFunctionality:

    @allure.title('Переход по клику на Конструктор.')
    def test_click_on_constructor_button(self, browser):
        page = HomePage(browser)
        page.click_constructor_button()
        assert Urls.HOME_PAGE_URL == page.get_current_url()

    @allure.title('Переход по клику на Лента заказов.')
    def test_click_on_order_feed_button(self, browser):
        page = HomePage(browser)
        page.click_order_feed_button()
        assert Urls.ORDER_FEED_URL == page.get_current_url()

    @allure.title('Получаем Детали ингредиента.')
    def test_click_on_ingredient(self, browser):
        page = HomePage(browser)
        page.click_ingredient()
        assert "Детали ингредиента" == page.get_element_text(HomePageLocators.card_ingredient_label)

    @allure.title('Закрываем Детали ингредиента кликом по крестику.')
    def test_exit_from_ingredient_card(self, browser):
        page = HomePage(browser)
        page.click_ingredient()
        page.wait_visibility_of_element(HomePageLocators.card_ingredient_label)
        page.exit_ingredient_card()
        assert page.wait_visibility_of_element(HomePageLocators.main_page_title)

    @allure.title('Проверяем увеличение счетчика при добавлении ингредиента в заказ.')
    def test_check_counter_increase(self, browser):
        page = HomePage(browser)
        count_before = int(page.get_element_text(HomePageLocators.count))
        page.drag_and_drop_ingredient(HomePageLocators.Bun_ingredient, HomePageLocators.basket)
        count_after = int(page.get_element_text(HomePageLocators.count))
        assert count_after > count_before

    @allure.title('Проверяем возможность создания заказа авторизованным пользователем')
    def test_check_order_creation(self, browser, register):
        page = PersonalAccountPage(browser)
        page.open_url(Urls.HOME_PAGE_URL)
        page.do_login(register[0], register[1])
        page.drag_and_drop_ingredient(HomePageLocators.Bun_ingredient, HomePageLocators.basket)
        page.click_place_order_button()
        assert page.wait_visibility_of_element(HomePageLocators.active_order_label)
