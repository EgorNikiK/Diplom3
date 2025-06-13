from selenium.webdriver.common.by import By


class HomePageLocators:

    main_page_title = (By.XPATH, ".//h1[text()='Соберите бургер']")
    constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    order_feed_button = (By.XPATH, ".//p[text()='Лента Заказов']")
    Bun_ingredient = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
    card_ingredient_label = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    exit_ingredient_button = (By.XPATH, "//button[@class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    count = (By.XPATH, ".//p[@class='text text_type_digits-medium mr-3']")
    basket = (By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']")
    place_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    active_order_label = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")

class OrderFeedPageLocators:

    order_feed_label = (By.XPATH, ".//h1[text()='Лента Заказов']")
    order = (By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6']")
    order_card_label = (By.XPATH, ".//p[text()='Cостав']")
    all_orders_counter = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    today_orders_counter = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    order_in_feed = (By.XPATH, "(//div[contains(@class, 'OrderHistory_dataBox__1mkxK')])[1]")
    order_in_work = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    completed_orders = (By.XPATH, ".//ul[@class='OrderFeed_orderList__cBvyi']")

class LoginPageLocators:

    login_page_title = (By.XPATH, "//div[@class='Auth_login__3hAey']")
    recovery_password_button = (By.XPATH, ".//a[text()='Восстановить пароль']")

class PersonalAccountPageLocators:

    personal_account_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    entrance_label = (By.XPATH, ".//h2[text()='Вход']")
    profile_label = (By.XPATH, ".//a[text()='Профиль']")
    password_field = (By.XPATH, ".//input[@name='Пароль']")
    email_field = (By.XPATH, ".//input[@name='name']")
    order_history_button = (By.XPATH, ".//a[text()='История заказов']")
    order_in_account = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    entrance_button = (By.XPATH, ".//button[text()='Войти']")
    exit_button = (By.XPATH, ".//button[text()='Выход']")

class RecoveryPasswordPageLocators:

    recovery_password_page_title = (By.XPATH, "//div[@class='Auth_login__3hAey']")
    input_email = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
    recovery_button = (By.XPATH, ".//button[text()='Восстановить']")
    save_button = (By.XPATH, ".//button[text()='Сохранить']")
    password_hide_show_button = (By.XPATH,".//div[@class='input__icon input__icon-action']")
    password_field = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
