import pytest
from selenium.webdriver.common.by import By
import time
import math

#import for selest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link="https://stepik.org/lesson/236895/step/1"


def test_open_and_author(browser):
    wait = WebDriverWait(browser, timeout=10, poll_frequency=0.2)

    browser.get(link)
    button_log_in = wait.until(EC.presence_of_element_located((By.ID, "ember499")))
    button_log_in.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "id_login_email")))
    email_input.send_keys("dmbochka")

    input_pass = wait.until(EC.presence_of_element_located((By.ID, "id_login_password")))
    input_pass.send_keys("ep...")

    button_log1 = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
    button_log1.click()

    # button_log = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sign-form__btn.button_with-loader.btn")))
    # button_log.click()
    time.sleep(10)
