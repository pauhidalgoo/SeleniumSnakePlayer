from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from plyer import notification

def up(x=0.05):
    time.sleep(x)
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()
def do(x=0.05):
    time.sleep(x)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
def tr(x=0.05):
    time.sleep(x)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
def lt(x=0.05):
    time.sleep(x)
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()


record = 0

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com/search?q=SNAKE&rlz=1C1VDKB_es&oq=SNAKE&aqs=chrome..69i57l2j69i59l2j0i271l2.474j0j7&sourceid=chrome&ie=UTF-8")
l =driver.find_element("xpath", "//div[text()='Aceptar todo']")
l.click()
s =driver.find_element("xpath", "//div[text()='Accept all']")
s.click()
c =driver.find_element("xpath", "//div[contains(@class, 'FL0z2d iIs7Af')]")
c.click()
time.sleep(1)
driver.implicitly_wait(2)
d =driver.find_element("xpath", "//div[contains(@class, 'e1XC2b')]")
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN)
actions.perform()
time.sleep(0.5)
actions.send_keys(Keys.ARROW_DOWN)
actions.perform()
time.sleep(0.5)
actions.send_keys(Keys.ARROW_DOWN)
actions.perform()

time.sleep(0.5)
actions.send_keys(Keys.ARROW_RIGHT)
actions.perform()
time.sleep(0.5)
actions.send_keys(Keys.ARROW_RIGHT)
actions.perform()
time.sleep(0.5)


for _ in range(100):
    r =driver.find_element("xpath", "//div[contains(@class, 'FL0z2d Uxkl7b')]")
    r.click()
    time.sleep(5)
    actions.send_keys(Keys.ARROW_DOWN)

    actions.perform()

    tile = 0.179
    tr(7*tile)
    up(12*tile)
    while (not driver.find_element("xpath", "//div[contains(@class, 'wjOYOd')]").is_displayed()):
        i = 0
        while(i<7):
            lt(14*tile)
            do(tile-0.025)
            lt(14*tile)
            up(tile-0.025)
            i += 1
        i = 0
        while(i<7):
            tr(14*tile)
            do(tile - 0.025)
            tr(14*tile)
            up(tile - 0.025)
            i += 1

    z = int(driver.find_element("xpath", "//div[contains(@class, 'HIonyd')]").text)
    if int(z)>record:
        record = int(z)
        notification.notify(
            title = 'New Record',
            message = "Enhorabona, has aconseguit " + str(record) + " pomes :)",
            app_icon = None,
            timeout = 10,)
    time.sleep(5)
driver.close()