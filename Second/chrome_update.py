from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Эта строка сама скачивает нужный драйвер и прописывает путь к нему
service = Service(executable_path=ChromeDriverManager().install())

# Запуск браузера
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")