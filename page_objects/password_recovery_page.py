from page_objects.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from helpers import *
import allure


class PasswdRecoveryPage(BasePage):
    @allure.step('Подождать загрузки кнопки "Восстановить пароль"')
    def wait_for_loading_button_recover_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.RECOVER_PASSWORD_BUTTON_ON_THE_LOGIN_SCREEN)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_the_recover_password_button(self):
        self.click_on_element(PasswordRecoveryLocators.RECOVER_PASSWORD_BUTTON_ON_THE_LOGIN_SCREEN)

    @allure.step('Проверить отображение поля email')
    def check_displaying_of_input_email(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.EMAIL_INPUT_FIELD)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.EMAIL_INPUT_FIELD)
        email = create_random_email()
        self.send_keys_to_input(PasswordRecoveryLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Подождать загрузки кнопки "Восстановить"')
    def wait_for_loading_button_recover(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.RESTORE_BUTTON_ON_THE_EMAIL_INPUT_PAGE)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.click_on_element(PasswordRecoveryLocators.RESTORE_BUTTON_ON_THE_EMAIL_INPUT_PAGE)

    @allure.step('Проверить отображение поля password')
    def check_displaying_of_input_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_FIELD)
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_FIELD)

    @allure.step('Ввести password')
    def send_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_FIELD)
        passwd = create_random_password()
        self.send_keys_to_input(PasswordRecoveryLocators.PASSWORD_FIELD, passwd)

    @allure.step('Подождать загрузки иконки глаза в поле ввода пароля')
    def wait_for_the_eye_icon_loading_in_the_password_entry_field(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.ICON_THAT_HIDER_THE_PASSWORD)

    @allure.step('Кликнуть на иконку глаза в поле ввода пароля')
    def click_on_eye_icon(self):
        self.click_on_element(PasswordRecoveryLocators.ICON_THAT_HIDER_THE_PASSWORD)

    @allure.step('Проверить, что значение поля password отображается')
    def check_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_WITH_VISIBILITY_STATUS)

    @allure.step('Проверить, что значение поля password не отображается')
    def check_not_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_HIDDEN)

