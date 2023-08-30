import yaml
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   # импорт сервиса для хрома
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager          # импорт модулей для firwfox и chrome


with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']

# service = Service(testdata['driver_path'])   # инициализировали сервис
# options = webdriver.ChromeOptions()           # инициализируем стандартные опции для хрома

class Site:
    def __init__(self, address):
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())  # автоматически скачивать  и устанавливать нужный вебдрайвер менеджер
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)      # инициализация драввйреа
        self.driver.implicitly_wait(3)   # ожидание
        self.driver.maximize_window()          # открыть браузер во все окно
        self.driver.get(address)                 #открыть сайт
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode, path):    # метод поиска элементов, передаем режим, путь
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):        # получение свойств элемента
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):   # закрытие соединения
        self.driver.close()