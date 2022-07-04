from browser import Browser
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep
from selenium.webdriver.common.keys import Keys


class Sign_in_page(Base_page):

    # Sectiune de identificare a elementelor
    EMAIL_INPUT = (By.XPATH,f'//input[@placeholder="Enter your email"]')
    PASS_INPUT= (By.XPATH,f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTONS = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PASSWORD_LINK= (By.LINK_TEXT,"Forgot password?")
    PASS_ERROR = (By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')
    SIGN_UP = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')

    # sectiune de definire a actiunilor pe care le putem face in raport cu elementele
    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/")

    def set_email(self,email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pass(self,password):
        self.chrome.find_element(*self.PASS_INPUT).send_keys(password)
        sleep(2)
        print('password input')


    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTONS).click()

    def clear_pass(self):
        self.chrome.find_element(*self.PASS_INPUT).send_keys(Keys.BACKSPACE)

    def click_forgot_password_link(self):
        self.chrome.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def check_current_url(self):
        expected_url = 'https://jules.app/sign-in'
        self.verify_url(expected_url)

    def check_error_pass(self):                                                         # rezolvare tema 12 ex.1
        expected = 'Please enter your password!'
        actual = self.chrome.find_element(*self.PASS_ERROR).text
        self.assertEqual(expected,actual,'The message error is not displayed')

    def check_login_button_is_disabled(self):
        button=self.chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[3]')  #rezolvare tema 12 ex.1
        if button is True:
            print('The button in not disableb')
        else:
            print('The button is disabled')


    def sign_up_page(self):
        self.chrome.finde_element(*self.SIGN_UP).click()


    # step definition (o agregare de pasi mici care au logica sa fie sub o singura umbrela/functie)
    def user_login(self, email, password):
        self.set_email(email)
        self.set_pass(password)
        self.click_login_button()

