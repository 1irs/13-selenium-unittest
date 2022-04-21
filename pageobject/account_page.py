from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage


class AccountPage(BasePage):

    """Под каждую страницу мы пишем отдельный PageObject"""

    def get_url(self) -> str:
        return 'http://tutorialsninja.com/demo/index.php?route=account/account'

    def is_present(self) -> bool:
        edit_account_link = self.driver.find_elements(By.LINK_TEXT, 'Edit your account information')
        return len(edit_account_link) == 1
