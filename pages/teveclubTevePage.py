from playwright.sync_api import Page, Locator


class TeveclubTevePage:
    def __init__(self, page: Page):
        self.page = page
        self.numberOfFoodSelect = self.page.locator("select[name='kaja']")
        self.numberOfFoodOwnerCanGiveOption = self.numberOfFoodSelect.locator("option")
        self.numberOfDrinkSelect = self.page.locator("select[name='pia']")
        self.numberOfDrinkOwnerCanGiveOption = self.numberOfDrinkSelect.locator("option")
        self.giveFoodAndDrinkInput = self.page.locator("input[name='etet']")

    def test_give_food_and_drink_to_teve(self):
        print("test_give_food_and_drink_to_teve starts now")
        if self.giveFoodAndDrinkInput.is_visible():
            self.numberOfFoodSelect.scroll_into_view_if_needed()
            self.numberOfFoodSelect.click()
            last_index_of_food_to_give = self.numberOfFoodOwnerCanGiveOption.count() - 1
            number_of_days_to_give_food = self.numberOfFoodOwnerCanGiveOption.nth(last_index_of_food_to_give).get_attribute("value")
            print(f"Give food for {number_of_days_to_give_food} days")
            self.numberOfFoodSelect.select_option(value=number_of_days_to_give_food)

            last_index_of_drink_to_give = self.numberOfDrinkOwnerCanGiveOption.count() - 1
            number_of_days_to_give_drink = self.numberOfDrinkOwnerCanGiveOption.nth(last_index_of_drink_to_give).get_attribute("value")
            print(f"Give drink for {number_of_days_to_give_drink} days")
            self.numberOfDrinkSelect.select_option(value=number_of_days_to_give_drink)
            self.giveFoodAndDrinkInput.click()
        else:
            print("The food and drink already filled")
        print("test_give_food_and_drink_to_teve ends now")
