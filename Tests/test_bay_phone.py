"""The test should fall like when the user saw the laptop that the price is displayed in dollars ($)
After he entered the cart, the currency  is not displayed there """

import pytest

from Pages.iphone_bay import Phone_Bay


@pytest.mark.usefixtures("init_driver")
class Test_Phone_Cart:

    @pytest.mark.xfail
    def test_bay_phone(self):
        self.PhoneBlank = Phone_Bay(self.driver)

        self.PhoneBlank.clic_iphone()# click in the catalog on the Phones

        self.PhoneBlank.clic_samsung()# click on the selected product (in our case) "Samsung galaxy s6"

        self.PhoneBlank.clic_add_to_cart()# Price of the selected item "Add to cart"

        self.PhoneBlank.clos_popup()# Close popup window after button click  'Add to cart'

        price_phone = self.PhoneBlank.text_in_price_phone()# Price of the selected item

        self.PhoneBlank.clic_cart()# Click on the cart to go to it

        catalog_cart = self.PhoneBlank.text_in_catalog_cart()#Displaying the price of an item in the cart

        assert price_phone != catalog_cart #compare the price of the product at the stage of adding to the cart with the price of the product in the cart itself