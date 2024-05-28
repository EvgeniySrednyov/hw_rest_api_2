import os
from dotenv import load_dotenv
import pytest
import requests

URL = 'https://demowebshop.tricentis.com'
# LOGIN = 'mattdaimon@mail.com'
# PASSWORD = '123@qwe'

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
@pytest.fixture(scope='function')
def auth():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    result = requests.post(
        url=URL + '/login',
        data={'Email': {login}, 'Password': {password}},
        allow_redirects=False
    )
    cookie = result.cookies.get('NOPCOMMERCE.AUTH')
    return cookie
