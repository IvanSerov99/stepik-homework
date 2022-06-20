from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary[type='submit']")
    submit.click()
    #alert = browser.switch_to.alert
    #alert.accept()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, ".form-control#answer[name='text'][type='text']")
    input_answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary[type='submit']")
    submit.click()
finally:
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

