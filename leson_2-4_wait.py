from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    #submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary#book[style='margin-top: 20px;'][onclick='checkPrice();']")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price[style='display:inline;float:right']"), "$100"))
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary#book[style='margin-top: 20px;'][onclick='checkPrice();']")
    submit.click()
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, ".form-control#answer[name='text'][type='text']")
    input_answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary[type='submit']")
    submit.click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
