from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from .main_page import MainPage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        MainPage.go_to_login_page(self)
        
        assert "login" in self.browser.current_url, f"Link {self.browser.current_url} is incorrect, should be another with login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        temp = BasePage.is_element_present(self, *LoginPageLocators.LOGIN_FORM)
        assert temp, "Login form wasn't find"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        temp = BasePage.is_element_present(self, *LoginPageLocators.REGISTER_FORM)
        assert temp, "Register form wasn't find"