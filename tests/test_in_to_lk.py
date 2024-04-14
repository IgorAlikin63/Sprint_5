from conftest import driver
from locators import StellarBurgersLocators
from data import StellarBurgersUserData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgersSwitchToLKwithCorrectUserData:

    def test_switch_to_lk_with_correct_user_data_by_lk_link_click(self, driver):  #переход в ЛК по клику на линк Личного кабинета
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
