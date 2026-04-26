import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import for selest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link="https://www.mobile.de/ru"

@pytest.fixture()
def browser():
    print("\nstart browser for test......")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser......")
    browser.quit()

class TestMobileDe():
   
   #@pytest.mark.smoke   
    def test_main_dropdown_lists(self, browser):
        browser.get(link)
        time.sleep(5)
        #wait = WebDriverWait(browser, 10)
        button_agreed = browser.find_element(By.CSS_SELECTOR, ".mde-consent-accept-btn")
        button_agreed.click()
        time.sleep(5)
        # Вариант поиска через Select
        select_mark = Select(browser.find_element(By.ID, 'make-incl-0'))
        #select_mark.click()
        select_mark.select_by_value('1900')
        time.sleep(5)

        #ищем по классике
        #input_mark = browser.find_element(By.ID, "make-incl-0")
        #input_mark.click()
        #time.sleep(5)
       
        #select_mark = browser.find_element(By.CSS_SELECTOR,'[value="1900"]')
        #select_mark.click()

        #input_mark.click()
        #time.sleep(10)


