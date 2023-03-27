from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import os


class Test_Odev:
    def w8(self,location):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(location))

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.screenShotPhat = str(date.today())
        # Path(self.screenShotPhat).mkdir(exist_ok=True)
        os.makedirs("./Homework5/Wrong",exist_ok=True)
        os.makedirs("./Homework5/True",exist_ok=True)
        os.makedirs("./Homework5/Error_Button",exist_ok=True)
        os.makedirs("./Homework5/Ordering",exist_ok=True)
        self.inputName = self.driver.find_element(By.ID,"user-name")
        self.inputPassword = self.driver.find_element(By.ID,"password")
        self.loginButton = self.driver.find_element(By.ID,"login-button")

    def teardown_method(self):
        self.driver.quit()


    @pytest.mark.parametrize("name,password",[("locked_out_user","secret_sauce"),("random","c"),("random2","v")])
    def test_wrong_logins(self,name,password):
    
        self.w8((By.ID,"user-name"))
        self.inputName.click()
        self.inputName.send_keys(name)
        
        self.w8((By.ID,"password"))
        self.inputPassword.click()
        self.inputPassword.send_keys(password)
        
        self.w8((By.ID,"login-button"))
        self.loginButton.click()
        
        self.w8((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        errormessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        
        # self.driver.save_screenshot(f"{self.screenShotPhat}/Wrong/{name}.png")
        self.driver.save_screenshot(f"./Homework5/Wrong/{name}.png")
        if errormessage.text == "Epic sadface: Username and password do not match any user in this service":
            assert True
        elif errormessage.text == "Epic sadface: Sorry, this user has been locked out.":
            assert True
        else:
            assert False

    @pytest.mark.parametrize("name,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])
    def test_true_logins(self,name,password):        
       
        self.w8((By.ID,"user-name"))
        self.inputName.click()
        self.inputName.send_keys(name)
        
        self.w8((By.ID,"password"))
        self.inputPassword.click()
        self.inputPassword.send_keys(password)
       
        self.w8((By.ID,"login-button"))
        self.loginButton.click()
        
        self.w8((By.XPATH,"//*[@id='root']"))
        self.driver.save_screenshot(f"./Homework5/True/{name}.png")
        newTarayici = self.driver.find_element(By.XPATH,"//*[@id='root']")
        
        assert newTarayici.is_displayed


    def test_errorButton(self):
        self.w8((By.ID,"user-name"))
        self.inputName.click()
        self.inputName.send_keys("Error Button")
        
        self.w8((By.ID,"password"))
        self.inputPassword.click()
        self.inputPassword.send_keys("x")

        self.w8((By.ID,"login-button"))
        self.loginButton.click()

        self.w8((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button"))
        button1 = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        self.driver.save_screenshot("./Homework5/Error_Button/Button.png")
        button1.click()
        self.driver.save_screenshot("./Homework5/Error_Button/notButton.png")



    def test_oredering(self):
        self.w8((By.ID,"user-name"))
        self.inputName.click()
        self.inputName.send_keys("standard_user")

        self.w8((By.ID,"password"))
        self.inputPassword.click()
        self.inputPassword.send_keys("secret_sauce")

        self.w8((By.ID,"login-button"))
        self.loginButton.click()

        self.w8((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))
        add_cart1 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        add_cart1.click()
        add_cart2 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        add_cart2.click()

        shopping_container = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        shopping_container.click()
        
        self.w8((By.ID,"checkout"))
        chekout = self.driver.find_element(By.ID,"checkout")
        chekout.click()

        self.w8((By.ID,"first-name"))
        self.driver.find_element(By.ID,"first-name").send_keys("Batuhan")
        self.driver.find_element(By.ID,"last-name").send_keys("sifre123")
        self.driver.find_element(By.ID,"postal-code").send_keys("9/012")
        self.driver.find_element(By.ID,"continue").click()

        self.w8((By.ID,"finish"))
        self.driver.save_screenshot("./Homework5/Ordering/confirm.png")
        self.driver.find_element(By.ID,"finish").click()

        self.w8((By.ID,"back-to-products"))
        self.driver.save_screenshot("./Homework5/Ordering/Ordering_done.png")


        
        









        
       



       
        
