from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Firstname")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Lastname")

    email = browser.find_element_by_name("email")
    email.send_keys("email@email.com")
    
    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname('C:\\Edu\\'))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'ex.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
