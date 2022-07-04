from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep


class Sign_up_page(Base_page):
    SIGN_UP = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    ERROR_MESSAGE_EMAIL = (By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/p')
    PERS_BUTTON = (By.XPATH, '//input[@value="personal"]')
    INPUT_EMAIL = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    CONTINUE_EMAIL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')
    CONTINUE_PASS_BUTTON = (By.CLASS_NAME, 'MuiButton-label')
    CONTINUE_LAST_PASSWORD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[8]/button/span[1]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    CONTINUE_SIGN_UP_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')

    def navigate_sign_up_page(self):
        self.chrome.find_element(*self.SIGN_UP).click()

    def click_sign_up_button(self):
        self.chrome.find_element(*self.SIGN_UP).click()
        sleep(1)

    def click_personal_button(self):
        pers_button = self.chrome.find_element(*self.PERS_BUTTON)
        pers_button.click()
        sleep(1)

    def click_continue_button(self):
        sleep(1)
        self.chrome.find_element(By.XPATH, '//button[@data-test-id="select-account-continue-btn"]').click()

    def input_first_name(self, name):
        self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input').send_keys(name)
        sleep(1)

    def click_continue_first_name_button(self):
        self.chrome.find_element(By.XPATH, '//button[@data-test-id="first-name-continue-btn"]').click()
        sleep(1)

    def input_last_name(self, last_name):
        self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input').send_keys(
            last_name)
        sleep(1)

    def click_last_name_continue_button(self):
        self.chrome.find_element(By.XPATH,
                                 "//div[@id='root']/div/div[4]/div[2]/div/div[3]/button[@data-test-id='last-name-continue-btn']").click()
        sleep(1)

    def input_email(self, email):
        self.chrome.find_element(*self.INPUT_EMAIL).send_keys(email)
        sleep(1)

    def check_error_message_email(self):
        expected = 'Please enter a valid email address.'
        actual = self.chrome.find_element(*self.ERROR_MESSAGE_EMAIL).text
        self.assertEqual(expected, actual, 'the error is different')
        sleep(1)

    def clear_email(self):
        self.chrome.find_element(*self.INPUT_EMAIL).clear()
        sleep(1)

    def check_error_messages_not_displayed(self):
        try:
            expected = 'Please enter a valid email address.'
            actual = self.chrome.find_element(*self.ERROR_MESSAGE_EMAIL).text
            self.assertEqual(expected, actual, 'the error is different')
        except:
            print('The error messages wos not vizible, the input adress was wright')

    def click_continue_email_button(self):
        self.chrome.find_element(*self.CONTINUE_EMAIL_BUTTON).click()
        sleep(1)

    def input_password(self, password):
        self.chrome.find_element(*self.INPUT_PASSWORD).send_keys(password)
        sleep(1)

    def check_continue_button(self):
        try:
            self.chrome.find_element(*self.CONTINUE_LAST_PASSWORD_BUTTON).is_displayed()

            sleep(1)
        except:
            print('continue_last_pass_button is not displayed')

    def clear_input_password(self):
        self.chrome.find_element(*self.INPUT_PASSWORD).clear()

        sleep(1)

    def set_password(self, password):
        self.chrome.find_element(*self.INPUT_PASSWORD).send_keys(password)
        sleep(3)

    def clic_continue_last_pass_button(self):
        button = self.chrome.find_element(*self.CONTINUE_LAST_PASSWORD_BUTTON)
        button.click()
        sleep(1)

    def confirm_password(self, password):
        self.chrome.find_element(*self.INPUT_PASSWORD).send_keys(password)
        sleep(1)

    def click_confirm_password_button(self):
        self.chrome.find_element(*self.CONTINUE_SIGN_UP_BUTTON).click()