from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service

from faker import Faker

from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support import expected_conditions as ES

from selenium.webdriver.support.ui import WebDriverWait

import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_clic(self,by_locator):# check function click() method, mouse click
        WebDriverWait(self.driver,10).until(ES.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):# the function executes the send_keys() method, data input
        WebDriverWait(self.driver, 10).until(ES.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):#the function performs the output of information in the form of text
        element = WebDriverWait(self.driver, 10).until(ES.visibility_of_element_located(by_locator))
        return  element.text

    def is_visible(self, title):#displays title as text
        WebDriverWait(self.driver, 10).until(ES.title_is(title))
        return  self.driver.title

    def clos_the_popup (self):# closing windows with a delay of 5 seconds
        time.sleep(5)
        return  Alert(self.driver).accept()

    def text_clos_the_popup (self):# closing windows with a delay of 5 seconds by taking the text of that window
        time.sleep(5)
        return  Alert(self.driver).text

    def usernamre(self,by_locator):
        fake = Faker()
        username = fake.name()
        WebDriverWait(self.driver, 10).until(ES.visibility_of_element_located(by_locator)).send_keys(username)

    def password(self, by_locator):
        fake = Faker()
        password = fake.password()
        WebDriverWait(self.driver, 10).until(ES.visibility_of_element_located(by_locator)).send_keys(password)


