import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from helpers import *
import requests
from urls import Urls
import allure

logger = logging.getLogger(__name__)

@pytest.fixture(params=[webdriver.Chrome,webdriver.Firefox], ids=['chrome','firefox'], scope="function")
def driver(request):
    """Фикстура инициализирует драйвер для Firefox и Chrome с одинаковыми параметрами."""
    driver_class = request.param

    if driver_class == webdriver.Chrome:
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)

    elif driver_class == webdriver.Firefox:
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        PROFILE = FirefoxProfile()
        PROFILE.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = PROFILE
        driver = webdriver.Firefox(options=firefox_options)

    driver.get(Urls.BASE_URL)
    logger.info(f'Инициализирован драйвер: {driver_class.__name__}')
    yield driver
    driver.quit()
    logger.info(f'Закрыт драйвер: {driver_class.__name__}')


@pytest.fixture
def generate_user_credentials():
    email = create_random_email()
    password = create_random_password()
    name = create_random_name()
    return email, password, name


@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными кредами и удаляет его из базы после теста')
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(Urls.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ для его аккаунта')
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [
        '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
        '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79'
    ]}
    response_body = requests.post(Urls.ORDER_CREATE, data=payload, headers=headers)

    yield access_token, response_body
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура передает в драйвер токены созданного пользователя')
def set_user_tokens(driver, create_new_user_and_delete):
    driver.get(Urls.BASE_URL)
    user_data = create_new_user_and_delete[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')