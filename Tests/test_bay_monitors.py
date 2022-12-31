"""Тест должен упасть так как когда пользователь выбрал  монитор  мы видим что цена отображаеться в  долларах($)
После того как он переходит в корзину, там не отоброжаеться валюта """

import pytest

from Pages.monitors_bay import Monitors_Bay


@pytest.mark.usefixtures("init_driver")
class Test_Monotors:

    @pytest.mark.xfail
    def test_bay_phone(self):
        self.Monitors = Monitors_Bay(self.driver)

        self.Monitors.click_monitors()# click in the catalog on the Monitors

        self.Monitors.clic_apple_monitor()# click on the selected product (in our case) "Apple monitor 24"

        prace_monitor = self.Monitors.text_prace_monitor()# Price of the selected item

        self.Monitors.clic_add_to_cart() # Price of the selected item "Add to cart" "Add to cart"

        self.Monitors.clos_popup()# Close popup window after button click  'Add to cart'

        self.Monitors.clic_cart()# Click on the cart to go to it

        prace_monitor_cart = self.Monitors.text_prace_moninor_cart()#Displaying the price of an item in the cart

        assert prace_monitor != prace_monitor_cart #compare the price of the product at the stage of adding to the cart with the price of the product in the cart itself
