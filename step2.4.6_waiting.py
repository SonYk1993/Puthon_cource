from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

# Ожидаем до 10 сек, но проверяем каждые 0.2 сек (200 мс)

wait = WebDriverWait(browser, timeout=10, poll_frequency=0.2)
button = wait.until(EC.presence_of_element_located((By.ID, "verify")))

#button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text