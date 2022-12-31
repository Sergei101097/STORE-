from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

class Sign_Up(BasePage):

    SING_UP = (By.ID, "signin2")
    SING_UP_PULL = (By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
    SIN = (By.XPATH, "//*[@id='signInModalLabel']")

    def __init__(self, driver):
        super().__init__(driver)

    def clic_sing_up(self):

        return self.do_clic(self.SING_UP)

    def clic_sing_up_pul(self):

         return self.do_clic(self.SING_UP_PULL)

    def clos_popup(self):
        return  self.clos_the_popup()

    def name_text(self):

        return self.get_element_text(self.SIN)

