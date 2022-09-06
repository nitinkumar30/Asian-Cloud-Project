import time
import pyautogui

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

from assets.variable import *  # Importing everything from variable.py
from assets.xpaths import *  # Importing everything from xpaths.py

# -------------------------------------
# Automatically downloads chromedriver compatible with the current chrome browser
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)


# -------------------------------------


def take_ss(full_path):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(full_path)
    time.sleep(2)


# opening the url
driver.get(loginUrl)
time.sleep(5)
take_ss(r'screenshots/homepage.png')


# Login function to perform login functionality
def login():
    try:
        driver.find_element(By.XPATH, xpath_username).clear()
        driver.find_element(By.XPATH, xpath_username).send_keys(mail)
        take_ss(r'screenshots/login/1.png')
        driver.find_element(By.XPATH, xpath_password).clear()
        driver.find_element(By.XPATH, xpath_password).send_keys(pswd)
        take_ss(r'screenshots/login/2.png')
        driver.find_element(By.XPATH, xpath_rememberMeLink).click()
        take_ss(r'screenshots/login/3.png')
        driver.find_element(By.XPATH, xpath_loginBtn).click()
        take_ss(r'screenshots/login/4.png')

    except:
        print('Exception occurred', )


# Signup function to perform Registeration functionality
def signup():
    try:
        driver.find_element(By.XPATH, xpath_registerLink).click()
        take_ss(r'screenshots/signup/1.png')
        time.sleep(2)
        driver.find_element(By.XPATH, xpath_mail).send_keys(mail_new)
        take_ss(r'screenshots/signup/2.png')
        driver.find_element(By.XPATH, xpath_password).send_keys(pswd_new)
        take_ss(r'screenshots/signup/3.png')
        driver.find_element(By.XPATH, xpath_passwordConfirm).send_keys(pswd_new)
        take_ss(r'screenshots/signup/4.png')
        print("The enabled condition of Back to Login link is {}.".format(
            driver.find_element(By.XPATH, xpath_backToLoginBtn).is_displayed()))
        driver.find_element(By.XPATH, xpath_registerBtn).click()
        take_ss(r'screenshots/signup/5.png')

    except:
        print("Exception occurred.")


# forgot Password function to perform password forgetting functionality
# It'll call the login method just after submitting
def forgotPass():
    try:
        driver.find_element(By.XPATH, xpath_forgotPasswordLink).click()
        take_ss(r'screenshots/forgotPass/1.png')
        time.sleep(2)
        driver.find_element(By.XPATH, xpath_username).send_keys(mail)
        take_ss(r'screenshots/forgotPass/2.png')
        driver.find_element(By.XPATH, xpath_submitBtn).click()
        take_ss(r'screenshots/forgotPass/3.png')

        login()  # Calling login method to login after confirming the mail id

    except:
        print("Exception occurred.")


# To check the functionalities:-

# login()  # Login Functionality
# signup()  # Signup functionality
forgotPass() # Forgot password functionality

time.sleep(5)
driver.close()
