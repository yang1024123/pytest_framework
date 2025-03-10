from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 创建ChromeOptions对象
options = Options()
# 设置detach选项为True
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

url = "http://10.10.106.250:19972/#/loginPage"
try:
    driver.get(url)
    driver.maximize_window()

    username_input = driver.find_element(By.XPATH, "//input[@type='text']")
    username_input.send_keys("yw")

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys("123456")

    login_button = driver.find_element(By.XPATH, "//button[@type='button']")
    login_button.click()
finally:
    print("测试完成")