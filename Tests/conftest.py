"""Запуск  Chrome Браузера"""

from Config.config import DataTest

import pytest

from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):

    options = webdriver.ChromeOptions()

    options.headless = True

    ff_driver = webdriver.Chrome(executable_path=DataTest.CHROME_PATH, options=options)

    request.cls.driver = ff_driver

    ff_driver.get("https://www.demoblaze.com/")

    yield