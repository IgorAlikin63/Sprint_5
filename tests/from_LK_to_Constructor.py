#переход из ЛК в Конструктор по клику на «Конструктор»
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим ко входу в аккаунт по клику на "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#заполняем валидные данные для входа
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("igor_alikin_07_123@mail.ru")
driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys("qwerty123")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()

time.sleep(2)

#переходим в ЛК по клику на "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

time.sleep(2)

#проверяем, что произошел переход в профиль
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

#переходим в конструктор по клику на "Конструктор"
driver.find_element(By.LINK_TEXT, "Конструктор").click()

#проверяем, что произошел переход в конструктор
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# Закрой браузер
driver.quit()

#переход из ЛК в Конструктор по клику на логотип Stellar Burgers
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим ко входу в аккаунт по клику на "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#заполняем валидные данные для входа
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("igor_alikin_07_123@mail.ru")
driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys("qwerty123")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()

time.sleep(2)

#переходим в ЛК по клику на "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

time.sleep(2)

#проверяем, что произошел переход в профиль
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

#переходим в конструктор по клику на логотип Stellar Burgers
driver.find_element(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2").click()

#проверяем, что произошел переход в конструктор
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# Закрой браузер
driver.quit()