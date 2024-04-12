from conftest import driver
from locators import StellarBurgersLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStellarBurgersTabChanges:

    def test_change_to_fillings_by_tab_click(self, driver): #проверяем переход к блоку начинок в списке по клику на вкладку "Начинки"
        fillings_tab_in_ingredients_constructor = driver.find_element(*StellarBurgersLocators.FILLINGS_TAB_IN_INGREDIENTS_CONSTRUCTOR) #переходим к вкладке Начинки, чтобы вызвать скролл списка
        fillings_tab_in_ingredients_constructor.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.FILLINGS_HEADER_IN_INGREDIENTS_LIST)))

        assert driver.find_element(*StellarBurgersLocators.FILLINGS_HEADER_IN_INGREDIENTS_LIST).is_displayed() #проверяем, заголовок "Начинки" отображается в списке и список до него проскроллился

    def test_change_to_sauce_by_tab_click(self, driver): #проверяем переход к блоку соусов в списке по клику на вкладку "Соусы"
        fillings_tab_in_ingredients_constructor = driver.find_element(*StellarBurgersLocators.FILLINGS_TAB_IN_INGREDIENTS_CONSTRUCTOR)  #переходим к вкладке Начинки, чтобы вызвать скролл списка
        fillings_tab_in_ingredients_constructor.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.FILLINGS_HEADER_IN_INGREDIENTS_LIST)))

        sauce_tab_in_ingredients_constructor = driver.find_element(*StellarBurgersLocators.SAUCE_TAB_IN_INGREDIENTS_CONSTRUCTOR) #переходим к вкладке Соусы, чтобы вызвать скролл списка
        sauce_tab_in_ingredients_constructor.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.SAUCE_HEADER_IN_INGREDIENTS_LIST)))

        assert driver.find_element(*StellarBurgersLocators.SAUCE_HEADER_IN_INGREDIENTS_LIST).is_displayed()  #проверяем, заголовок "Соусы" отображается в списке и список до него проскроллился

    def test_change_to_bun_by_tab_click(self, driver):  #проверяем переход к блоку соусов в списке по клику на вкладку "Булки"
        fillings_tab_in_ingredients_constructor = driver.find_element(*StellarBurgersLocators.FILLINGS_TAB_IN_INGREDIENTS_CONSTRUCTOR)  #переходим к вкладке Начинки, чтобы вызвать скролл списка
        fillings_tab_in_ingredients_constructor.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.FILLINGS_HEADER_IN_INGREDIENTS_LIST)))

        bun_tab_in_ingredients_constructor = driver.find_element(*StellarBurgersLocators.BUN_TAB_IN_INGREDIENTS_CONSTRUCTOR) #переходим к вкладке Булки, чтобы вызвать скролл списка
        bun_tab_in_ingredients_constructor.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((StellarBurgersLocators.BUN_HEADER_IN_INGREDIENTS_LIST)))

        assert driver.find_element(*StellarBurgersLocators.BUN_HEADER_IN_INGREDIENTS_LIST).is_displayed()  #проверяем, заголовок "Булки" отображается в списке и список до него проскроллился

