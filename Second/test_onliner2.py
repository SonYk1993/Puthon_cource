from selenium.webdriver.common.by import By
import time


link = "https://www.onliner.by"

def test_guest_reg(browser):
    browser.get(link)
    time.sleep(3)
    y = 'Полина добрая девочка1!'*45

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(10)


    
