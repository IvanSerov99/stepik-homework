from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select
file_path = os.path.join("C:/Users/iserov/Desktop/", 'Test.txt')
#def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    #x = x_element.text
    #y = calc(x)
    #check = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotCheckbox[type='checkbox']")
    #check.click()
    #radio = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotsRule[type='radio'][name='ruler'][value='robots']")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    #radio.click()
    first_name = browser.find_element(By.CSS_SELECTOR, ".form-control[type='text'][name='firstname'][placeholder='Enter first name']")
    first_name.send_keys('Ivan')
    second_name = browser.find_element(By.CSS_SELECTOR, ".form-control[type='text'][name='lastname'][placeholder='Enter last name']")
    second_name.send_keys('Ivan')
    third_name = browser.find_element(By.CSS_SELECTOR, ".form-control[type='text'][name='email'][placeholder='Enter email']")
    third_name.send_keys('Ivan')
    upload_file = browser.find_element(By.CSS_SELECTOR, "#file[type='file'][name='file'][accept='.txt']")
    upload_file.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary[type='submit'][style='margin-top: 40px;']")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
