"""The test should fall like when the user saw the laptop that the price is displayed in dollars ($)
After he entered the cart, the currency  is not displayed there """
import pytest

from Pages.laptops_bay import Laptops_Bay


@pytest.mark.usefixtures("init_driver")
class Test_Laptops_Cart:

    @pytest.mark.xfail
    def test_bay_latpops(self):
        self.LaptopsBay = Laptops_Bay(self.driver)

        self.LaptopsBay.clic_laptops()# click in the catalog on the laptops

        self.LaptopsBay.click_sony()# click on the selected product (in our case) "Sony vaio i5"

        prace_sony = self.LaptopsBay.prace_sony_laptops()# Price of the selected item

        self.LaptopsBay.clicl_add_to_cart()# Price of the selected item "Add to cart"

        self.LaptopsBay.clos_popup()# Close popup window after button click  'Add to cart'

        self.LaptopsBay.click_cart()# Click on the cart to go to it

        prace_sony_cart = self.LaptopsBay.prace_sonu_in_cart()#Displaying the price of an item in the cart

        assert prace_sony != prace_sony_cart #compare the price of the product at the stage of adding to the cart with the price of the product in the cart itself
