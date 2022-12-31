"""The user must enter their login details"""
import pytest

from Config.config import DataTest

from Pages.log_In import Log_In

@pytest.mark.usefixtures("init_driver")
class Test_Log_In:

    def test_sing_up(self):
        self.loginPage = Log_In(self.driver)

        self.loginPage.clic_log_in()#click on phone brand 'Log in'

        self.loginPage.input_username_password(DataTest.USERNAME, DataTest.PASSWORD)# filling in the login fields

        self.loginPage.clic_log_in_exit()#click on the button after entering data for registration 'Log in'

        info_txt_local = self.loginPage.text_in_pole_registers()# Upload the account that we successfully logged into

        assert info_txt_local == "Welcome SergeiKLimenkov097"#check if the user has logged into his account after entering his data