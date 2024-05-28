import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser, have

URL = 'https://demowebshop.tricentis.com'
def test_login(auth):
    response = requests.post(url=URL + '/addproducttocart/details/72/1',
                            data={'product_attribute_72_5_18': 53,
                                  'product_attribute_72_6_19': 54,
                                  'product_attribute_72_3_20': 57,
                                  'addtocart_72.EnteredQuantity': 1},
                            cookies={'NOPCOMMERCE.AUTH': auth}
                            )

    with allure.step('Открытие интернет-магазина'):
        browser.open(URL)
        browser.driver.add_cookie({'name' : 'NOPCOMMERCE.AUTH', 'value' : auth})
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with allure.step('Открытие корзины'):
        browser.open(URL + '/cart')

    with allure.step('Добавление товара в корзину'):
        browser.element('.product-name').should(have.text("Build your own cheap computer"))

    with allure.step('Проверка добавленного товара в корзине'):
        browser.element('.product-subtotal').should(have.text("815.00"))
        browser.element('.qty-input').should(have.value("1"))