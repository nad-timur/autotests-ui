from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.user_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')


    def fill(self, email: str, user: str, password: str):
        self.email_input.fill(email)
        self.user_input.fill(user)
        self.password_input.fill(password)


    def check_visible(self, email: str, user: str, password: str):
        expect(self.email_input).to_have_value(email)
        expect(self.user_input).to_have_value(user)
        expect(self.password_input).to_have_value(password)