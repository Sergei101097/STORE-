from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

class Laptops_Bay(BasePage):

    LAPTOPS = (By.LINK_TEXT, "Laptops")
    SONY_VAIO_I5 = (By.LINK_TEXT, "Sony vaio i5")
    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")
    CART = (By.ID, "cartur")
    PRACE_SONY = (By.XPATH, "//*[@id='tbodyid']/h3")
    PRACE_SONY_CART = (By.XPATH, "//*[@id='tbodyid']/tr/td[3]")

    def clic_laptops(self):
        return  self.do_clic(self.LAPTOPS)

    def click_sony(self):
        return self.do_clic(self.SONY_VAIO_I5)

    def clicl_add_to_cart(self):
        self.do_clic(self.ADD_TO_CART)

    def click_cart(self):
        return self.do_clic(self.CART)


    def prace_sony_laptops(self):
        return self.get_element_text(self.PRACE_SONY)



    def prace_sonu_in_cart(self):
        return self.get_element_text(self.PRACE_SONY_CART)[0:4]

    def clos_popup(self):
          return self.clos_the_popup()


