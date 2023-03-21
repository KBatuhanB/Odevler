from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        test1Result = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test 1(Boş Bırakma): {test1Result}")
        sleep(1)
        driver.refresh()
        sleep(1)
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage2 = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        test2Result = errorMessage2.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test 2(Yasaklı Kullanıcı): {test2Result}")
        sleep(1)
        driver.refresh()
        sleep(1)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("Batuhan Bölükbaşı")
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage3 = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        test3Result = errorMessage3.text == "Epic sadface: Password is required"
        print(f"Test 3(Şifre Boş Bırakma): {test3Result}")



    def close_button(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        X_button = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        X_button.click()
        sleep(3)

    def correct_Login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        products = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        print(f"Ürün Sayısı: {len(products)}")






        

tests = Test()
tests.test_invalid_login()
tests.close_button()
tests.correct_Login()

