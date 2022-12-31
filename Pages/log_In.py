from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

class Log_In(BasePage):

    LOG_IN = (By.ID, "login2")

    USERNAME = (By.ID, "loginusername")

    PASSWORD = (By.ID, "loginpassword")

    EXIT_LOG_IN = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")

    ELEMENT_TEXT = (By.ID, "nameofuser")

    def __init__(self, driver):
        super().__init__(driver)

    def clic_log_in(self):
        return self.do_clic(self.LOG_IN)

    def input_username_password(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)

    def clic_log_in_exit(self):
        return self.do_clic(self.EXIT_LOG_IN)

    def text_in_pole_registers(self):
        return  self.get_element_text(self.ELEMENT_TEXT)