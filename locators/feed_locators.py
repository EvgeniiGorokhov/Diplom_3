from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Раздел заказов
    ORDERS_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    TITLE_OF_ORDERS_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Карточка заказа в ленте
    ORDER_CARD_IN_THE_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Всплывающее окно с деталями заказа
    POPUP_WINDOW_WITH_ORDER_DETAILS = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                                                 '(@class, "Modal_orderBox")]')

    # Заголовок всплывающего окна с деталями заказа
    POPUP_TITLE_WITH_ORDER_DETAILS = (
        By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                  '"Modal_orderBox")]//h2')

    # Счетчик заказов "Выполнено за все время"
    ORDER_COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик заказов "Выполнено за сегодня"
    ORDER_COUNTER_COMPLETED_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Заказ в разделе "В работе"
    ORDER_IN_THE_IN_PROGRESS_SECTION = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')

    # Номер заказа в разделе "В работе"
    ORDER_NUMBER_IN_THE_IN_PROGRESS_SECTION = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')

    # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
    ID_ORDER_CARD_IN_FEED_WITH_SUBSTITUTIONS = (By.XPATH, './/*[text()="{order_id}"]')
