from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

time.sleep(3)  # sleep for 3 sec

sign_in = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]").click()

email = driver.find_element(By.NAME, "email").send_keys("olhasamchuk7@gmail.com")
password = driver.find_element(By.NAME, "password").send_keys("00X4Ka*7w1x8")
true = driver.find_element(By.NAME, "remember").click()
login = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]").click()
time.sleep(5)

edit = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li[2]/app-car/div/div[1]/div[2]/button[1]").click()
time.sleep(3)
remove_car = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-edit-car-modal/div[3]/button").click()
time.sleep(3)
remove = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-remove-car-modal/div[3]/button[2]").click()
time.sleep(3)

assert "Car removed" in driver.page_source

driver.close()