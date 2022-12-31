"""The test should pass if the user successfully registers on the site"""
import pytest

from Pages.registr_sity import Registration

@pytest.mark.usefixtures("init_driver")
class Test_Registration:

    def test_registration(self):
        self.Registration = Registration(self.driver)

        self.Registration.clic_sign_in()#lick on phone brand  'Sign in'

        self.Registration.input_name_password()#data entry (name and password)

        self.Registration.clic_sign_up()#lick on phone brand  'Sign up'

        re = self.Registration.text_clos_the_popup()#text from the future window that tells us about successful registration

        assert re == "Sign up successful."# check the text with the one that should appear upon successful registration

