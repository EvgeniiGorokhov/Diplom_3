from selenium.webdriver.common.by import By


class MainLocators:
    # Кнопка "Войти в аккаунт" на главной
    BUTTON_LOG_IN_TO_YOUR_ACCOUNT_ON_THE_MAIN_PAGE = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    # Кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]' )
    # Кнопка "Оформить заказ"
    PLACE_AN_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    # Кнопка "Конструктор" в шапке сайта
    CONSTRUCTOR_BUTTON_IN_THE_SITE_HEADER = (By.XPATH, '//p[text() = "Конструктор"]')
    # Заголовок раздела "Конструктор"
    HEADING_OF_THE_CONSTRUCTOR_SECTION = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')
    # Заголовок раздела "Булки" в меню конструктора
    HEADING_OF_THE_BUNS_SECTION_IN_THE_CONSTRUCTOR_MENU = (By.XPATH, '//span[text() = "Булки"]')
    # Заголовок раздела "Соусы" в меню конструктора
    HEADING_OF_THE_SAUCES_SECTION_IN_THE_CONSTRUCTOR_MENU = (By.XPATH, '//span[text() = "Соусы"]')
    # Заголовок раздела "Начинки" в меню конструктора
    HEADING_OF_THE_FILLINGS_SECTION_IN_THE_CONSTRUCTOR_MENU = (By.XPATH, '//span[text() = "Начинки"]')
    # Кнопка "Лента заказов"
    SUBMIT_ORDER_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    # Ингредиент
    INGREDIENT = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
    # Заголовок окна "Детали ингредиента"
    WINDOW_TITLE_INGREDIENT_DETAILS = (
        By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    BUTTON_WITH_A_CROSS_THAT_CLOSES_THE_INGREDIENT_DETAILS = (By.XPATH, '//section[contains(@class, '
                                                                        '"Modal_modal_opened")]//button[contains(@class, "close")]')
    # Картинка ингредиента в общем списке
    PICTURE_OF_THE_INGREDIENT_IN_THE_GENERAL_LIST = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    # Куда перетаскиваются ингредиенты
    WHERE_ARE_THE_INGREDIENTS_DRAGGED = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    # Состав заказа в условной "Корзине"
    CONTENTS_OF_THE_ORDER_IN_THE_CONDITIONAL_BASKET = (
        By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')
    # Количество экземпляров ингредиента в заказе (счетчик)
    NUMBER_OF_INGREDIENT_COPIES_IN_THE_ORDER_COUNTER = (
        By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                  '@class="counter_counter__num__3nue1"][1]')
    # Окно подтверждения создания заказа
    ORDER_CREATION_CONFIRMATION_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                                    '(@class, "Modal_modal__container")]')
    # Номер созданного заказа в окне подтверждения
    NUMBER_OF_THE_CREATED_ORDER_IN_THE_CONFIRMATION_WINDOW = (
        By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    BUTTON_WITH_A_CROSS_THAT_CLOSES_THE_CONFIRMED_ORDER_WINDOW = [By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]


