#меняем вкладки
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переходим к вкладке Начинки, чтобы вызвать скролл списка
driver.find_element(By.XPATH, "//span[contains(@class,'text text_type_main-default') and contains(text(),'Начинки')]").click()

time.sleep(1)

#проверяем отображение заголовка "Начинки" в списке под вкладками на экране при помощи is_displayed
assert driver.find_element(By.XPATH, "//h2[contains(@class,'text text_type_main-medium mb-6 mt-10') and contains(text(),'Начинки')]").is_displayed()

time.sleep(1)

#переходим к вкладке Соусы, чтобы вызвать скролл списка
driver.find_element(By.XPATH, "//span[contains(@class,'text text_type_main-default') and contains(text(),'Соусы')]").click()

time.sleep(1)

#проверяем отображение заголовка "Соусы" в списке под вкладками на экране при помощи is_displayed
assert driver.find_element(By.XPATH, "//h2[contains(@class,'text text_type_main-medium mb-6 mt-10') and contains(text(),'Соусы')]").is_displayed()

time.sleep(1)

#переходим к вкладке Булки, чтобы вызвать скролл списка
driver.find_element(By.XPATH, "//span[contains(@class,'text text_type_main-default') and contains(text(),'Булки')]").click()

time.sleep(1)

#проверяем отображение заголовка "Булки" в списке под вкладками на экране при помощи is_displayed
assert driver.find_element(By.XPATH, "//h2[contains(@class,'text text_type_main-medium mb-6 mt-10') and contains(text(),'Булки')]").is_displayed()

#Закрой браузер
driver.quit()
