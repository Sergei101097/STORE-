"""The test should be skipped because the information from the website is not correct to what should be there"""

import pytest

from Config.config import Info_Phone

from Pages.info_phone_6 import Phone_Iphone_6

@pytest.mark.usefixtures("init_driver")
class Test_Info_Phone:

    @pytest.mark.xfail
    def test_sing_up(self):
        self.Info_Phone = Phone_Iphone_6(self.driver)

        self.Info_Phone.clic_iphone_6()#click on phone brand "Iphone 6 32 gb"

        info_text = self.Info_Phone.info_iphone()#phone information

        assert info_text != Info_Phone.IPHONE_6#comparison of information from the site with information that should be