import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

from assets.variable import *  # Importing everything from variable.py
from assets.xpaths import *   # Importing everything from xpaths.py

# -------------------------------------
# Automatically downloads chromedriver compatible with the current chrome browser
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

# -------------------------------------
# opening the url
driver.get(loginUrl)
time.sleep(5)


# Login function to perform login functionality
def login():
    try:
        driver.find_element(By.XPATH, xpath_username).send_keys(mail)
        driver.find_element(By.XPATH, xpath_password).send_keys(pswd)
        driver.find_element(By.XPATH, xpath_rememberMeLink).click()
        driver.find_element(By.XPATH, xpath_loginBtn).click()

    except:
        print('Exception occurred', )


# Signup function to perform Registeration functionality
def signup():
    try:
        driver.find_element(By.XPATH, xpath_registerLink).click()
        time.sleep(2)
        driver.find_element(By.XPATH, xpath_mail).send_keys(mail_new)
        driver.find_element(By.XPATH, xpath_password).send_keys(pswd_new)
        driver.find_element(By.XPATH, xpath_passwordConfirm).send_keys(pswd_new)
        driver.find_element(By.XPATH, xpath_registerBtn).click()
        print("The enabled condition of Back to Login link is {}.".format(
            driver.find_element(By.XPATH, xpath_backToLoginBtn).is_displayed()))

    except:
        print("Exception occurred.")


# forgot Password function to perform password forgetting functionality
# It'll call the login method just after submitting
def forgotPass():
    try:
        driver.find_element(By.XPATH, xpath_forgotPasswordLink).click()
        time.sleep(2)
        driver.find_element(By.XPATH, xpath_username).send_keys(mail_new)
        driver.find_element(By.XPATH, xpath_submitBtn).click()

        login()  # Calling login method to login after confirming the mail id

    except:
        print("Exception occurred.")


# To check the functionalities:-

login()  # Login Functionality
# signup() # Signup functionality
# forgotPass() # Forgot password functionality

time.sleep(5)
driver.close()
