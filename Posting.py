# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=1122 --user-data-dir="C:\Selenium\SavedChrome_Posting"


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as py

url = "https://www.instagram.com/staleman117/"


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:1122")
driver = webdriver.Chrome(executable_path = "C:\Selenium\chromedriver.exe", chrome_options = opt)

while True:
    PlusButton = driver.find_element(By.CLASS_NAME, "_acub")
    PlusButton.click()
    time.sleep(1)

    UploadButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
    UploadButton.click()
    time.sleep(1)

    py.write("C:\\Selenium\\ok.png")
    # time.sleep(1)
    py.press("enter")

    time.sleep(1)

    Next1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button')
    Next1.click()

    time.sleep(2)

    Next2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button')
    Next2.click()

    time.sleep(1)

    Share = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button')
    Share.click()

    time.sleep(3)

    Close = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]")
    Close.click()

    time.sleep(1)

    driver.refresh()

    time.sleep(300)