from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')
        self.user_input = Input(page, 'registration-form-username-input', 'User')

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.user_input.fill(username)
        self.password_input.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_have_value(email)
        self.user_input.check_have_value(username)
        self.password_input.check_have_value(password)

