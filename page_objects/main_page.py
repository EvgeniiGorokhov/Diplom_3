from selenium.webdriver import ActionChains

from page_objects.base_page import BasePage
from locators.main_locators import MainLocators
import allure


class MainPage(BasePage):
    @allure.step('Подождать загрузки кнопки "Личный кабинет"')
    def wait_for_the_personal_account_button_to_load(self):
        self.wait_visibility_of_element(MainLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Кликнуть по кнопке  личный кабинет в хэдере')
    def click_on_personal_account_in_header(self):
        self.click_on_element(MainLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Подождать загрузки кнопки "Лента заказов"')
    def wait_for_the_order_feed_button_to_load(self):
        self.wait_visibility_of_element(MainLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.click_on_element(MainLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Подождать загрузки кнопки "Конструктор"')
    def wait_for_the_constructor_button_to_load(self):
        self.wait_visibility_of_element(MainLocators.CONSTRUCTOR_BUTTON_IN_THE_SITE_HEADER)

    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON_IN_THE_SITE_HEADER)

    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        return self.get_text_on_element(MainLocators.HEADING_OF_THE_CONSTRUCTOR_SECTION)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        self.click_on_element(MainLocators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT_ON_THE_MAIN_PAGE)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_visibility_of_element(MainLocators.ORDER_CREATION_CONFIRMATION_WINDOW)
        return self.check_displaying_of_element(MainLocators.ORDER_CREATION_CONFIRMATION_WINDOW)

    @allure.step('Подождать загрузки ингредиентов')
    def wait_for_ingredients_to_load(self):
        self.wait_visibility_of_element(MainLocators.INGREDIENT)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(MainLocators.INGREDIENT)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        self.wait_visibility_of_element(MainLocators.WINDOW_TITLE_INGREDIENT_DETAILS)
        return self.check_displaying_of_element(MainLocators.WINDOW_TITLE_INGREDIENT_DETAILS)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(MainLocators.WINDOW_TITLE_INGREDIENT_DETAILS)
        if not self.check_displaying_of_element(MainLocators.WINDOW_TITLE_INGREDIENT_DETAILS):
            return True

    @allure.step('Подождать загрузки кнопки Х закрывающие детали ингредиента')
    def wait_for_the_X_button_to_load_closing_ingredient_details(self):
        self.wait_visibility_of_element(MainLocators.BUTTON_WITH_A_CROSS_THAT_CLOSES_THE_INGREDIENT_DETAILS)

    @allure.step('Кликнуть по кнопке "Х"')
    def click_on_the_X_button(self):
        self.click_on_element(MainLocators.BUTTON_WITH_A_CROSS_THAT_CLOSES_THE_INGREDIENT_DETAILS)

    @allure.step('Добавить интгридиенты')
    def drag_and_drop_ingredient_to_order(self):
        source_element = self.find_element_with_wait(MainLocators.PICTURE_OF_THE_INGREDIENT_IN_THE_GENERAL_LIST)
        target_element = self.find_element_with_wait(MainLocators.WHERE_ARE_THE_INGREDIENTS_DRAGGED)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainLocators.NUMBER_OF_INGREDIENT_COPIES_IN_THE_ORDER_COUNTER)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.click_on_element(MainLocators.PLACE_AN_ORDER_BUTTON)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        return self.check_displaying_of_element(MainLocators.ORDER_CREATION_CONFIRMATION_WINDOW)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_to_change_text(MainLocators.NUMBER_OF_THE_CREATED_ORDER_IN_THE_CONFIRMATION_WINDOW,
                                             '9999')
        return self.get_text_on_element(MainLocators.NUMBER_OF_THE_CREATED_ORDER_IN_THE_CONFIRMATION_WINDOW)

    @allure.step('Подождать загрузки кнопки Х закрывающая окно подтвержденного заказа')
    def wait_for_the_X_button_to_load_closing_the_confirmed_order_window(self):
        self.wait_visibility_of_element(MainLocators.BUTTON_WITH_A_CROSS_THAT_CLOSES_THE_CONFIRMED_ORDER_WINDOW)

    @allure.step('Кликнуть по кнопке "Х" закрывающая окно подтвержденного заказа')
    def click_on_the_X_button_to_close_the_confirmed_order_window(self):
        self.click_on_element(MainLocators.BUTTON_WITH_A_CROSS_THAT_CLOSES_THE_CONFIRMED_ORDER_WINDOW)








