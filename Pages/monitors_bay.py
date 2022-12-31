from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

class Monitors_Bay(BasePage):

    MONITORS = (By.LINK_TEXT, "Monitors")
    APPLE_MONITOR_24 = (By.LINK_TEXT, "Apple monitor 24")
    PRACE_MONITOR = (By.XPATH, "//*[@id='tbodyid']/h3")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    CART = (By.ID, "cartur")
    PRACE_MONITOR_CART = (By.XPATH, "//*[@id='tbodyid']/tr/td[3]")

    def click_monitors(self):
        return self.do_clic(self.MONITORS)

    def clic_apple_monitor(self):
        return self.do_clic(self.APPLE_MONITOR_24)

    def clic_add_to_cart(self):
        return self.do_clic(self.ADD_TO_CART)

    def clic_cart(self):
        return self.do_clic(self.CART)

    def clos_popup(self):
        return self.clos_the_popup()

    def text_prace_monitor(self):
        return self.get_element_text(self.PRACE_MONITOR)[0:4]

    def text_prace_moninor_cart(self):
        return self.get_element_text(self.PRACE_MONITOR_CART)