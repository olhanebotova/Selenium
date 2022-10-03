from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox")

# driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(service=Service('/Users/olhanebotova/Downloads/chromedriver'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")
# driver.get("https://qauto2.forstudy.space/")

time.sleep(3)  # sleep for 3 sec

sign_in = driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

email = driver.find_element(By.XPATH, "//input[@name='email']").send_keys("olhasamchuk7@gmail.com")
password = driver.find_element(By.XPATH, "//input[@name='password']").send_keys("00X4Ka*7w1x8")
true = driver.find_element(By.XPATH, "//div[@class='form-check']").click()
login = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
time.sleep(5)

mileage = driver.find_element(By.XPATH, "//input[@name='miles']").send_keys("1")
time.sleep(3)

update = driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
time.sleep(5)

assert "Mileage updated" in driver.page_source

driver.close()