from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Раздел "Профиль"
    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]')

    # Раздел "История заказов"
    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Кнопка "Выйти", логаут
    BUTTON_LOGOUT = (By.XPATH, '//button[@type = "button"]')

    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTER = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Описание раздела: "В этом разделе вы можете изменить свои персональные данные"
    DESCRIPTION_OF_SECTION = (By.XPATH, '//p[contains(@class, "Account_text")]')



   