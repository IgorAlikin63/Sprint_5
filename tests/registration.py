#Поле имя не пустое
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим к разделу регистрации
driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

#переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

#в форме регистрации не заполняем поле Имя, заполняем остальные и пробуем зарегистрироваться
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("privet123@gmail.com")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("redstar123")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

#проверяем, что не произошел переход на /login и мы все еще на /register
assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'

# Закрой браузер
driver.quit()

#Ошибка пароля менее 6ти символов

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим к разделу регистрации
driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

#переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

#в форме регистрации в поле пароля вводим менее 6ти символов
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").click()

#проверяем, что отобразилась ошибка
assert 'Некорректный пароль' in driver.find_element(By.CSS_SELECTOR, ".input__error").text

# Закрой браузер
driver.quit()

#Корректная регистрация с верными данными
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим к разделу регистрации
driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

#переходим к форме регистрации нового пользователя кликая на "Зарегистрироваться"
driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

#в форме регистрации не заполняем поле Имя, заполняем остальные и пробуем зарегистрироваться
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Борис")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("privet4122@gmail.com") #чтобы отработал корректно нужна новая почта, т.к. не может повторяться
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("redstar123")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

time.sleep(2)

#проверяем, что произошел переход на /login
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

# Закрой браузер
driver.quit()