from conftest import driver
from locators import StellarBurgersLocators
from data import StellarBurgersUserData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStellarBurgersUserLogin:

    def test_login_with_main_page_button(self, driver):
        login_into_account_main_page_button = driver.find_element(*StellarBurgersLocators.LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON)  #переходим к логину
        login_into_account_main_page_button.click()

        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  # заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)

        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  # заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)

        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)  #кликаем на кнопку Войти
        lk_login_user_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON)))

        assert driver.find_element(*StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON).is_displayed() #проверяем отображение кнопки "Оформить заказ" т.к. она появляется после успешного логина

    def test_login_with_lk_link(self, driver): #вход через кнопку «Личный кабинет»
        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE)  # переходим в ЛК по линку Личный кабинет
        lk_link_main_page.click()

        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  # заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)

        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  #заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)

        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)  #кликаем на кнопку Войти
        lk_login_user_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON)))

        assert driver.find_element(*StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON).is_displayed()  #проверяем отображение кнопки "Оформить заказ" т.к. она появляется после успешного логина

    def test_login_from_link_in_registration_form(self, driver): #вход через кнопку в форме регистрации
        login_into_account_main_page_button = driver.find_element(*StellarBurgersLocators.LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON)  #переходим к логину
        login_into_account_main_page_button.click()

        registration_link_for_new_user = driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK_FOR_NEW_USER)  #переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
        registration_link_for_new_user.click()

        login_link_in_registration_form = driver.find_element(*StellarBurgersLocators.LOGIN_LINK_IN_REGISTRATION_FORM) #переходим по линку "Войти" в форме регистрации
        login_link_in_registration_form.click()

        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  #заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)

        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  #заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)

        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)# кликаем на кнопку Войти
        lk_login_user_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON)))

        assert driver.find_element(*StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON).is_displayed() #проверяем отображение кнопки "Оформить заказ" т.к. она появляется после успешного логина

    def test_login_from_link_in_remind_password_form(self, driver): #вход через кнопку восстановления пароля
        login_into_account_main_page_button = driver.find_element(*StellarBurgersLocators.LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON)  #переходим к логину
        login_into_account_main_page_button.click()

        remind_password_link_in_login_form = driver.find_element(*StellarBurgersLocators.REMIND_PASSWORD_LINK_IN_LOGIN_FORM) #переходим к форме восстановления пароля через линк "Восстановить пароль"
        remind_password_link_in_login_form.click()

        login_link_in_remind_password_form = driver.find_element(*StellarBurgersLocators.LOGIN_LINK_IN_REMIND_PASSWORD_FORM) #переходим к форме входа через линк "Войти"
        login_link_in_remind_password_form.click()

        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  # заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)

        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  # заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)

        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)  # кликаем на кнопку Войти
        lk_login_user_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON)))

        assert driver.find_element(*StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON).is_displayed() #проверяем отображение кнопки "Оформить заказ" т.к. она появляется после успешного логина
