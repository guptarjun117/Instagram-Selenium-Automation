# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=2233 --user-data-dir="C:\Selenium\SavedChrome_DM"


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:2233")
driver = webdriver.Chrome(executable_path = "C:\Selenium\chromedriver.exe", chrome_options = opt)

dm_type = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

dm_type.click()

# time.sleep(1)

dm_type.send_keys("this is a test text")

# time.sleep(1)

dm_type.send_keys(Keys.ENTER)
