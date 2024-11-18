from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Кнопка «Восстановить пароль» на экране входа в систему
    RECOVER_PASSWORD_BUTTON_ON_THE_LOGIN_SCREEN = (By.XPATH, '//a[text() = "Восстановить пароль"]')
    # Поле ввода email
    EMAIL_INPUT_FIELD = (By.CLASS_NAME, 'input__textfield')
    # Кнопка "Восстановить" на странице ввода email
    RESTORE_BUTTON_ON_THE_EMAIL_INPUT_PAGE = (By.CLASS_NAME, 'button_button__33qZ0')
    # Поле ввода пароля
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    # Иконка, скрывающая пароль
    ICON_THAT_HIDER_THE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    # Пароль со статусом видимости
    PASSWORD_WITH_VISIBILITY_STATUS = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                                 '"input_status_active")]')
    # Пароль скрыт
    PASSWORD_HIDDEN = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                 '"input_type_password")]')
