import time
from conftest import driver
from locators import StellarBurgersLocators
from data import StellarBurgersUserData


class TestStellarBurgersSwitchToLKwithCorrectUserData:

    def test_switch_to_lk_with_correct_user_data_by_lk_link_click(self,driver):  #переход в ЛК по клику на линк Личного кабинета
        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE) #переходим в ЛК по линку Личный кабинет
        lk_link_main_page.click()
        lk_login_user_email = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_EMAIL)  #заполняем поле почта
        lk_login_user_email.send_keys(*StellarBurgersUserData.AUTH_EMAIL)
        lk_login_user_password = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_PASSWORD)  #заполняем поле пароль
        lk_login_user_password.send_keys(*StellarBurgersUserData.AUTH_PASSWORD)
        lk_login_user_button = driver.find_element(*StellarBurgersLocators.LK_LOGIN_USER_BUTTON)  #кликаем на кнопку Войти
        lk_login_user_button.click()
        time.sleep(2)
        lk_link_main_page = driver.find_element(*StellarBurgersLocators.LK_LINK_MAIN_PAGE)  #переходим в ЛК по клику на "Личный кабинет"
        lk_link_main_page.click()
        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'  #проверяем, что произошел переход в профиль


#переход в ЛК по клику на «Личный кабинет»
#from selenium.webdriver.common.by import By
#from selenium import webdriver
#import time

#driver = webdriver.Chrome()
#driver.get("https://stellarburgers.nomoreparties.site/")

#переходим ко входу в аккаунт по клику на "Личный кабинет"
#driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#заполняем валидные данные для входа
#driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("igor_alikin_07_123@mail.ru")
#driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys("qwerty123")
#driver.find_element(By.XPATH, "//button[text()='Войти']").click()

#time.sleep(2)

#переходим в ЛК по клику на "Личный кабинет"
#driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#time.sleep(2)

#проверяем, что произошел переход в профиль
#assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

# Закрой браузер
#driver.quit()