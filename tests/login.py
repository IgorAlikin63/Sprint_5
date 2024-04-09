#вход по кнопке «Войти в аккаунт» на главной
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим ко входу в аккаунт
driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

#заполняем валидные данные для входа
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("igor_alikin_07_123@mail.ru")
driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys("qwerty123")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()

time.sleep(2)

#проверяем, что произошел переход на /login
assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'

# Закрой браузер
driver.quit()

#вход через кнопку «Личный кабинет»
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

#проверяем, что произошел переход на /login
assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'

# Закрой браузер
driver.quit()

#вход через кнопку в форме регистрации
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим ко входу в аккаунт по клику на "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#переходим в раздел Зарегистрироваться
driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

#переходим в раздел Зарегистрироваться
driver.find_element(By.LINK_TEXT, "Войти").click()

#заполняем валидные данные для входа
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("igor_alikin_07_123@mail.ru")
driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys("qwerty123")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()

time.sleep(2)

#проверяем, что произошел переход на /login
assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'

# Закрой браузер
driver.quit()

#вход через кнопку восстановления пароля
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим ко входу в аккаунт по клику на "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#переходим в раздел Восстановить пароль
driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()

#переходим в раздел Войти
driver.find_element(By.LINK_TEXT, "Войти").click()

#заполняем валидные данные для входа
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("igor_alikin_07_123@mail.ru")
driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys("qwerty123")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()

time.sleep(2)

#проверяем, что произошел переход на /login
assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'

# Закрой браузер
driver.quit()