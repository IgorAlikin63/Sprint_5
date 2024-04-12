from conftest import driver
from locators import StellarBurgersLocators
from data import StellarBurgersUserData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStellarBurgersSwitchFromLKtoConstructor:

    def test_switch_from_lk_to_constructor_by_click_constructor_link(self, driver): #переход из ЛК в Конструктор по клику на «Конструктор»
        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE) #переходим в ЛК по линку Личный кабинет
        lk_link_main_page.click()

        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  #заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)

        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  #заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)

        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)  #кликаем на кнопку Войти
        lk_login_user_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON)))

        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE)  #переходим в ЛК по клику на "Личный кабинет"
        lk_link_main_page.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.PROFILE_SECTION_HEADER)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' #проверяем, что произошел переход в профиль

        constructor_link = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_LINK) #переходим в конструктор по клику на "Конструктор"
        constructor_link.click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' #проверяем, что произошел переход в конструктор

    def test_switch_from_lk_to_constructor_by_click_on_logo(self, driver): #переход из ЛК в Конструктор по клику на логотип Stellar Burgers
        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE) #переходим в ЛК по линку Личный кабинет
        lk_link_main_page.click()

        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  #заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)

        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  #заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)

        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)  #кликаем на кнопку Войти
        lk_login_user_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.CREATE_NEW_ORDER_BUTTON)))

        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE)  #переходим в ЛК по клику на "Личный кабинет"
        lk_link_main_page.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.PROFILE_SECTION_HEADER)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'  #проверяем, что произошел переход в профиль

        stellar_burgers_logo = driver.find_element(*StellarBurgersLocators.STELLAR_BURGERS_LOGO) #переходим в конструктор по клику на логотип
        stellar_burgers_logo.click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'  #проверяем, что произошел переход в конструктор













