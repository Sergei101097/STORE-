from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

class Phone_Bay(BasePage):

    PHONES  = (By.LINK_TEXT, "Phones")

    SAMSUNG_GALAXY_S6 = (By.LINK_TEXT, "Samsung galaxy s6")

    ADD_TO_CART = (By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")

    CART = (By.ID, "cartur")

    TEXT_PRICE_IN_CART = (By.XPATH, "//*[@id='tbodyid']/tr/td[3]")

    TEXT_PRICE_IPHONE = (By.XPATH, "//*[@id='tbodyid']/h3")



    def clic_iphone(self):
        return self.do_clic(self.PHONES)

    def clic_samsung(self):
        return self.do_clic(self.SAMSUNG_GALAXY_S6)

    def clic_add_to_cart(self):
        return self.do_clic(self.ADD_TO_CART)

    def clic_cart(self):
        return self.do_clic(self.CART)

    def text_in_catalog_cart(self):
        return self.get_element_text(self.TEXT_PRICE_IN_CART)

    def text_in_price_phone(self):
        t = self.get_element_text(self.TEXT_PRICE_IPHONE)
        j = t[0:4]
        return j

    def clos_popup(self):
          return self.clos_the_popup()



