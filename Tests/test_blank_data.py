"""If the user does not enter the registration data, and clicks the Login option,
the program will display an appropriate message stating that no data has been entered,
to enter them, you will need to close the expanding window """
import pytest

from Pages.sing_up import Sign_Up


@pytest.mark.usefixtures("init_driver")
class Test_Sing_Up:

    def test_sing_up(self):
        self.SignUp = Sign_Up(self.driver)

        self.SignUp.clic_sing_up()# click on the button 'Sing up'

        self.SignUp.clic_sing_up_pul()# after entering for registration, without filling in the field, click on the button 'Sing in'

        self.SignUp.clos_popup()# closed window

        text = self.SignUp.name_text()# text after the popup closes to make sure we're not kicked back to the main page

        assert text == 'Sign up'# check if the user stayed on the registration page or was thrown to the main page