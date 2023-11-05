from pages.base_page import BasePage
from locators.form_page_locators import FomPageLocators as locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = 'Hello'
        last_name = 'World'
        email = 'hello@world.com'
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE)
        self.element_is_visible(Locators.SUBJECT)
        self.element_is_visible(Locators.HOBBIES)
        self.element_is_visible(Locators.FILE_INPUT)
        self.element_is_visible(Locators.CURRENT_ADDRESS)
        self.element_is_visible(Locators.SUBMIT)


