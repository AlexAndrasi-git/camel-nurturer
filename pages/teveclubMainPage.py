from playwright.sync_api import Page, Locator, expect


class TeveClubMainPage:
    def __init__(self, page: Page):
        self.page = page
        self.usernameInput = self.page.locator("#focusme")
        self.passwordInput = self.page.locator("input[type='password']")
        self.loginButton = self.page.locator("input[type='image']")


    def test_login_with_valid_user(self, username: str, password: str):
        self.page.goto("https://teveclub.hu/")
        self.usernameInput.fill(username)
        self.passwordInput.fill(password)
        self.loginButton.click()
        expect(self.loginButton).to_be_hidden()
        print("Successful UI login, end of 'test_login_with_valid_user'")