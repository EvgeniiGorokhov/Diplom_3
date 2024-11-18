from locators.order_history_locators import OrderHistoryPageLocators
from page_objects.base_page import BasePage
import allure


class OrderHistoryPage(BasePage):

    @allure.step('Подождать прогрузки карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.ORDER_CARD)

    @allure.step('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_TITLE)

    @allure.step('Получить номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_ID)