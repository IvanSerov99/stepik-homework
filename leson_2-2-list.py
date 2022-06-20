from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    #y_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#num2")
    #y = y_element.text
    y = calc(x)
    check = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotCheckbox[type='checkbox']")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotsRule[type='radio'][name='ruler'][value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    input = browser.find_element(By.CSS_SELECTOR, ".form-control#answer[type='text']")
    input.send_keys(y)
    #select = Select(browser.find_element(By.CSS_SELECTOR, "select.custom-select#dropdown"))
    #select.select_by_visible_text(str(z))
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary[type='submit'][style='margin-bottom: 1000px;']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
