from selenium.webdriver.common.by import By

from Pages.BasePages import BasePage

class Phone_Iphone_6(BasePage):

        IPHONE_6_32_GB = (By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a')
        INFO_PHONE_6 = (By.XPATH, '//*[@id="more-information"]/p')

        def clic_iphone_6(self):
            return self.do_clic(self.IPHONE_6_32_GB)

        def info_iphone(self):
            return self.get_element_text(self.INFO_PHONE_6)

