from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import unittest
import os


load_dotenv()


class E2EUI(unittest.TestCase):

    def setUp(self):
        # запуск браузера
        self.driver = webdriver.Chrome()

    def test_auth(self):
        # тест на авторизацию и вход
        driver = self.driver
        # Получение данных с сайта
        driver.get('https://www.saucedemo.com/')

        # проверка полученного сайта
        assert 'Swag Labs' in driver.title

        # ввод данных для авторизации
        login = driver.find_element(By.CSS_SELECTOR, "#user-name")
        login.send_keys(os.getenv("NAME") + Keys.RETURN)
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys(os.getenv("PASSOWRD") + Keys.RETURN)
        button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        button.click()

        # вывод страницы с товарами
        item = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
        item.click()

        # вывод нужного товара
        backpack = driver.find_element(By.XPATH, '//*[@id="add-to-cart"]')
        backpack.click()

        # переход в корзину
        shopping = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        shopping.click()

        # проверка нахождения товара в корзине
        name_item = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link > div').text
        assert 'Sauce Labs Backpack' == name_item

        # переход к оформлению заказа
        checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')
        checkout.click()

        # заполнение формы заказа и переход для подтверждения
        # проверка элементов формы
        first_name = driver.find_element(By.ID, 'first-name')
        assert 'first-name' == first_name.get_attribute('id')
        first_name.send_keys('firstname')
        last_name = driver.find_element(By.ID, 'last-name')
        assert 'last-name' == last_name.get_attribute('id')
        last_name.send_keys('lastname')
        Zip = driver.find_element(By.ID, 'postal-code')
        assert 'postal-code' == Zip.get_attribute('id')
        Zip.send_keys('111111')
        cont = driver.find_element(By.CLASS_NAME, 'btn_action')
        cont.click()

        # подтверждение оформления заказа
        # проверка на успешное оформление
        fin = driver.find_element(By.ID, 'finish')
        fin.click()
        done = driver.find_element(By.CSS_SELECTOR, '#checkout_complete_container > h2')
        assert 'Thank you for your order!' == done.text

    def tearDown(self):
        # закрытие браузера
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
