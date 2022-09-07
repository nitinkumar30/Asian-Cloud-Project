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

def wait(time_in_s):
    time.sleep(time_in_s)


def take_ss(full_path):
    wait(2)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(full_path)


def clickBtn(xpath):
    driver.find_element(By.XPATH, xpath).click()
    wait(2)


def clearText(xpath):
    driver.find_element(By.XPATH, xpath).clear()
    wait(2)


def writeText(xpath, value):
    clearText(xpath)
    driver.find_element(By.XPATH, xpath).send_keys(value)
    wait(2)


def isDisplayed(xpath):
    rslt = driver.find_element(By.XPATH, xpath).is_displayed()
    wait(2)
    return rslt


# -------------------------------------


# opening the url
driver.get(loginUrl)
wait(5)
take_ss(r'screenshots/homepage.png')


# Login function to perform login functionality
def login(username, password):
    try:
        writeText(xpath_username, username)
        take_ss(r'screenshots/login/1.png')
        writeText(xpath_password, password)
        take_ss(r'screenshots/login/2.png')
        clickBtn(xpath_rememberMeLink)
        take_ss(r'screenshots/login/3.png')
        wait(2)
        clickBtn(xpath_loginBtn)
        take_ss(r'screenshots/login/4.png')

    except:
        print('Exception occurred', )


# Signup function to perform Registration functionality
def signup(mail, pswd):
    try:
        clickBtn(xpath_registerLink)
        take_ss(r'screenshots/signup/1.png')
        writeText(xpath_mail, mail)
        take_ss(r'screenshots/signup/2.png')
        writeText(xpath_password, pswd)
        take_ss(r'screenshots/signup/3.png')
        writeText(xpath_passwordConfirm, pswd_new)
        take_ss(r'screenshots/signup/4.png')
        print("The enabled condition of Back to Login link is {}.".format(isDisplayed(xpath_backToLoginBtn)))
        driver.find_element(By.XPATH, xpath_registerBtn).click()
        take_ss(r'screenshots/signup/5.png')

    except:
        print("Exception occurred.")


# forgot Password function to perform password forgetting functionality
# It'll call the login method just after submitting
def forgotPass(username):
    try:
        clickBtn(xpath_forgotPasswordLink)
        take_ss(r'screenshots/forgotPass/1.png')
        writeText(xpath_username, mail)
        take_ss(r'screenshots/forgotPass/2.png')
        clickBtn(xpath_submitBtn)
        take_ss(r'screenshots/forgotPass/3.png')

        # Calling login method to login after confirming the mail id
        login(mail, pswd)


    except:
        print("Exception occurred.")


# To check the functionalities:-

login(mail, pswd)  # Login Functionality
# signup(mail_new, pswd_new)  # Signup functionality
# forgotPass(mail)  # Forgot password functionality

wait(5)
driver.close()
