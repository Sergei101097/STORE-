from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

from faker import Faker# This library will allow me to generate a random username and password for registration

class Registration(BasePage):

    SIGN_IN = (By.ID, "signin2")
    INPUT_USERNAME = (By.ID, "sign-username")
    INPUT_PASSWORD = (By.ID, "sign-password")
    SIGN_UP = (By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
    fake = Faker()

    def clic_sign_in(self):
        return self.do_clic(self.SIGN_IN)

    def input_name_password(self):
        fake = Faker()
        username = fake.name()# Random name generation
        password = fake.password()#Random password generation

        self.do_send_keys(self.INPUT_USERNAME,  username)
        self.do_send_keys(self.INPUT_PASSWORD, password)

    def clic_sign_up(self):
        return self.do_clic(self.SIGN_UP)

    def text_popup(self):
        return self.text_clos_the_popup()