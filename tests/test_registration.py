from conftest import driver
from locators import StellarBurgersLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

class TestStellarBurgersRegistration:

    def test_registration_cant_be_empty_name_field(self, driver): #Поле имя не должно быть пустым
        login_into_account_main_page_button = driver.find_element(*StellarBurgersLocators.LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON) #переходим к логину
        login_into_account_main_page_button.click()

        registration_link_for_new_user = driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK_FOR_NEW_USER) #переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
        registration_link_for_new_user.click()

        email_input_in_registration_new_user_form = driver.find_element(*StellarBurgersLocators.EMAIL_INPUT_IN_REGISTRATION_NEW_USER_FORM) #заполняем поле почта
        email_input_in_registration_new_user_form.send_keys("privet123@gmail.com")

        password_input_in_registration_new_user_form = driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_IN_REGISTRATION_NEW_USER_FORM) #заполняем поле пароль
        password_input_in_registration_new_user_form.send_keys("123456")

        registration_button_in_new_user_form = driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON_IN_NEW_USER_FORM) #кликаем на кнопку зарегистрироваться
        registration_button_in_new_user_form.click()

        assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login' #проверяем, что не произошел переход на /login и мы все еще на /register

    def test_registration_error_with_less_then_6_simbols_password(self, driver): #Ошибка пароля менее 6ти символов
        login_into_account_main_page_button = driver.find_element(*StellarBurgersLocators.LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON)  #переходим к логину
        login_into_account_main_page_button.click()

        registration_link_for_new_user = driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK_FOR_NEW_USER)  #переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
        registration_link_for_new_user.click()

        password_input_in_registration_new_user_form = driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_IN_REGISTRATION_NEW_USER_FORM)  #заполняем поле пароль
        password_input_in_registration_new_user_form.send_keys("123")

        registration_button_in_new_user_form = driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON_IN_NEW_USER_FORM)  #кликаем на кнопку зарегистрироваться
        registration_button_in_new_user_form.click()

        assert driver.find_element(*StellarBurgersLocators.INCORRECT_PASSWORD_ERROR_TEXT).is_displayed() #проверяем отображается ли текст ошибки на экране

    def test_successfull_new_user_registration_with_correct_parameters(self, driver): #Корректная регистрация с верными данными
        fake = Faker()
        login_into_account_main_page_button = driver.find_element(*StellarBurgersLocators.LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON)  #переходим к логину
        login_into_account_main_page_button.click()

        registration_link_for_new_user = driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK_FOR_NEW_USER)  #переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
        registration_link_for_new_user.click()

        name__input_in_registration_new_user_form = driver.find_element(*StellarBurgersLocators.NAME_INPUT_IN_REGISTRATION_NEW_USER_FORM) #заполняем поле имя
        name__input_in_registration_new_user_form.send_keys(fake.name())

        email_input_in_registration_new_user_form = driver.find_element(*StellarBurgersLocators.EMAIL_INPUT_IN_REGISTRATION_NEW_USER_FORM)  #заполняем поле почта
        email_input_in_registration_new_user_form.send_keys(fake.email())

        password_input_in_registration_new_user_form = driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_IN_REGISTRATION_NEW_USER_FORM)  #заполняем поле пароль
        password_input_in_registration_new_user_form.send_keys("123456")

        registration_button_in_new_user_form = driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON_IN_NEW_USER_FORM)  #кликаем на кнопку зарегистрироваться
        registration_button_in_new_user_form.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.LOGIN_HEADER)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'  #проверяем, что произошел переход на /login


