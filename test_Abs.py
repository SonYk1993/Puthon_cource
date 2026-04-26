from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    
    # Этот метод будет выполняться перед каждым тестом (test_*)
    def setUp(self):
        self.browser = webdriver.Chrome()
        # Небольшая задержка для стабильности
        self.browser.implicitly_wait(5) 

    # Этот метод будет выполняться после каждого теста (test_*)
    def tearDown(self):
        # Ожидание перед закрытием для визуальной оценки
        time.sleep(3) 
        self.browser.quit()

    # Вспомогательный метод для заполнения формы (DRY principle)
    def fill_form_and_get_text(self, link):
        self.browser.get(link)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input3.send_keys("123@123.com")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Находим элемент с текстом подтверждения
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text

    def test_registration_page1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        actual_result_text = self.fill_form_and_get_text(link1)
        expected_result_text = "Congratulations! You have successfully registered!"
        
        # Проверка утверждения
        self.assertEqual(actual_result_text, expected_result_text, f"Текст на странице 1 не совпадает с ожидаемым. Ожидали: {expected_result_text}, Получили: {actual_result_text}")

    def test_registration_page2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        actual_result_text = self.fill_form_and_get_text(link2)
        expected_result_text = "Congratulations! You have successfully registered!"
        
        # Проверка утверждения
        self.assertEqual(actual_result_text, expected_result_text, 
                         f"Текст на странице 2 не совпадает с ожидаемым. Ожидали: {expected_result_text}, Получили: {actual_result_text}")

if __name__ == "__main__":
    # Запуск тестов через unittest runner
    unittest.main()