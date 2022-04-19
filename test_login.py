import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.email = 'test+19apr@example.com'
        self.email_incorrect = 'test+19aprasdfasdfasdfasd@example.com'
        self.password = 'asdfasdf'
        self.password_incorrect = '123123'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.close()

    def testOK(self):
        """Успешный вход существующим пользователем"""
        self.driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')

        # Нужно найти элементы управления.
        email_field = self.driver.find_element(By.ID, 'input-email')
        password_field = self.driver.find_element(By.ID, 'input-password')
        login_button = self.driver.find_element(By.CSS_SELECTOR, '[value=Login]')

        # Ввели тестовые данные и совершили действие.
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        login_button.click()

        # Нам нужно проверить, успешно ли мы залогинились?
        edit_account_link = self.driver.find_elements(By.LINK_TEXT, 'Edit your account information')

        # Сообщаем о том, прошел тест или нет.
        #self.assertEqual(1, len(edit_account_link))
        #assert 1 == len(edit_account_link)

    def test_not_ok(self):
        """Проверка на неправильный пароль"""
        self.driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')

        # Нужно найти элементы управления.
        email_field = self.driver.find_element(By.ID, 'input-email')
        password_field = self.driver.find_element(By.ID, 'input-password')
        login_button = self.driver.find_element(By.CSS_SELECTOR, '[value=Login]')

        # Ввели тестовые данные и совершили действие.
        email_field.send_keys(self.email)
        password_field.send_keys(self.password_incorrect)
        login_button.click()

        # Нам нужно проверить, успешно ли мы залогинились?
        alert_text = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        alert_text_value = alert_text.text

        # Сообщаем о том, прошел тест или нет.
        self.assertEqual(
            'Warning: No match for E-Mail Address and/or Password.',
            alert_text_value
        )

    def test_password_recovery(self):
        """Восстановление пароля"""
        self.driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')

        # Находим ссылку "Forgotten Password" и кликаем по ней.
        forgot_password_link = self.driver.find_element(By.LINK_TEXT, 'Forgotten Password')
        forgot_password_link.click()

        # Находим поле email и вводим его
        email_field = self.driver.find_element(By.ID, 'input-email')
        email_field.send_keys(self.email)

        # Находим кнопку Continue и кликаем по ней.
        continue_button = self.driver.find_element(By.CSS_SELECTOR, '[value=Continue]')
        continue_button.click()

        # Нам нужно проверить, успешно ли мы залогинились?
        alert_text = self.driver.find_element(By.CLASS_NAME, 'alert-success')
        actual_text = alert_text.text

        # Сообщаем о том, прошел тест или нет.
        expected_text = 'An email with a confirmation link has been sent your email address.'

        self.assertEqual(
            expected_text,
            actual_text
        )

    def test_password_recovery_not_fount(self):
        """Восстановление пароля на несуществующий имейл"""
        self.driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')

        # Находим ссылку "Forgotten Password" и кликаем по ней.
        forgot_password_link = self.driver.find_element(By.LINK_TEXT, 'Forgotten Password')
        forgot_password_link.click()

        # Находим поле email и вводим его
        email_field = self.driver.find_element(By.ID, 'input-email')
        email_field.send_keys(self.email_incorrect)

        # Находим кнопку Continue и кликаем по ней.
        continue_button = self.driver.find_element(By.CSS_SELECTOR, '[value=Continue]')
        continue_button.click()

        # Нам нужно проверить, успешно ли мы залогинились?
        alert_text = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        actual_text = alert_text.text

        # Сообщаем о том, прошел тест или нет.
        expected_text = 'Warning: The E-Mail Address was not found in our records, please try again!'

        self.assertEqual(
            expected_text,
            actual_text
        )
