from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    LOGIN_INTO_ACCOUNT_MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт" главная страница
    REGISTRATION_LINK_FOR_NEW_USER = (By.LINK_TEXT, "Зарегистрироваться") #ссылка "Зарегистрироваться" для новых пользователей в разделе Вход
    NAME_INPUT_IN_REGISTRATION_NEW_USER_FORM = (By.XPATH, ".//label[text() = 'Имя']/../input") #поле имя в форме "Регистрация" для новых пользователей
    EMAIL_INPUT_IN_REGISTRATION_NEW_USER_FORM = (By.XPATH, ".//label[text() = 'Email']/../input") #поле email в форме "Регистрация" для новых пользователей
    PASSWORD_INPUT_IN_REGISTRATION_NEW_USER_FORM = (By.XPATH, ".//label[text() = 'Пароль']/../input") #поле пароль в форме "Регистрация" для новых пользователей
    REGISTRATION_BUTTON_IN_NEW_USER_FORM = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" в форме "Регистрация" для новых пользователей
    INCORRECT_PASSWORD_ERROR_TEXT = (By.XPATH, ".//p[text() = 'Некорректный пароль']") #текст сообщения об ошибке в связи с некорректным паролем
    LK_LINK_MAIN_PAGE = (By.LINK_TEXT, "Личный Кабинет") #ссылка на личный кабинет с главной страницы
    LK_LOGIN_USER_EMAIL = (By.CSS_SELECTOR, "input[name='name']") #поле ввода email форма входа
    LK_LOGIN_USER_PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']") #поле ввода пароль форма входа
    LK_LOGIN_USER_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнопка Войти на форме авторизации в личный кабинет
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор") #ссылка на конструктор
    STELLAR_BURGERS_LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2") #логотип Stellar Burgers
    PROFILE_QUIT_BUTTON = (By.XPATH, "//button[text()='Выход']") #кнопка "Выход" в Личном кабинете
    CREATE_NEW_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") #кнопка "Офорить заказ" на главной, когда залогинены юзером
    LOGIN_LINK_IN_REGISTRATION_FORM = (By.LINK_TEXT, "Войти") #ссылка "Войти" в форме регистрации новых пользователей
    LOGIN_LINK_IN_REMIND_PASSWORD_FORM = (By.XPATH, "//a[(@href='/login')]") #ссылка "Войти" в форме восстановления пароля
    REMIND_PASSWORD_LINK_IN_LOGIN_FORM = (By.LINK_TEXT, "Восстановить пароль") #ссылка "Восстановить пароль" в разделе Вход
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']") #заголовок формы входа
    PROFILE_SECTION_HEADER = (By.XPATH, "//a[text()='Профиль']") #заголовок Профиль в личном кабинете
    FILLINGS_TAB_IN_INGREDIENTS_CONSTRUCTOR = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']") #вкладка Начинки в конструкторе бургеров
    FILLINGS_HEADER_IN_INGREDIENTS_LIST = (By.XPATH, "//h2[contains(@class,'text text_type_main-medium mb-6 mt-10') and contains(text(),'Начинки')]") #заголовок раздела Начинки в списке ингредиентов
    SAUCE_TAB_IN_INGREDIENTS_CONSTRUCTOR = (By.XPATH,"//span[@class='text text_type_main-default' and text()='Соусы']")  # вкладка Соусы в конструкторе бургеров
    SAUCE_HEADER_IN_INGREDIENTS_LIST = (By.XPATH,"//h2[contains(@class,'text text_type_main-medium mb-6 mt-10') and contains(text(),'Соусы')]")  # заголовок раздела Соусы в списке ингредиентов
    BUN_TAB_IN_INGREDIENTS_CONSTRUCTOR = (By.XPATH,"//span[@class='text text_type_main-default' and text()='Булки']")  # вкладка Булки в конструкторе бургеров
    BUN_HEADER_IN_INGREDIENTS_LIST = (By.XPATH,"//h2[contains(@class,'text text_type_main-medium mb-6 mt-10') and contains(text(),'Начинки')]")  # заголовок раздела Булки в списке ингредиентов