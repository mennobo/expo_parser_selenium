# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json
import shutil
import os

credentials = {
    'inUserName': 'LS23_BT24.User021@cr14.net',
    'inUserPass': '2fQbo#JQB2ca4%i9*YS*R487RJ^gxq#Su%^YGqzywFF$xEGCRwzuTgN!n^Skfvwp62pYB@5y^Y'
}


from selenium.webdriver.firefox.options import Options
options = webdriver.FirefoxOptions()
options.headless = True # This is normally the first google search after people find Selenium.
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r"C:\Users\peach\Documents\Projecten\Locked_shields_23\expo_parser\geckodriver.exe", options=options)

# =============================================================================
# 
# # chrome setup
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\peach\Documents\Projecten\Locked_shields_23\chromedriver.exe")
# 
# =============================================================================

#driver = webdriver.PhantomJS(executable_path=r"C:\phantomjs-2.1.1-windows\bin\phantomjs.exe")

url = "https://expo.berylia.org/"
new_url = "https://expo.berylia.org/availability"

# Grabbing a URL using the browser instance.
driver.get(url)
sleep(2)

# Logging in
uname = driver.find_element("id", "username") 
uname.send_keys(credentials['inUserName'])
uname = driver.find_element("id", "password") 
uname.send_keys(credentials['inUserPass'])

# Click sign in button to login the website.
driver.find_element("id", "kc-login").click()

# We need sleepers to not be locked out
sleep(2)

# go to availability page
driver.get(new_url)

sleep(2)

# find all the rows
content = driver.find_elements(By.CLASS_NAME, "expandedInactiveRow")

# fill a dictionary to convet to json
content_dict = dict()
for index, item in enumerate(content):
    text = item.text.split(' ')
    content_dict[text[0]] = {
        "Zone": text[1],
        "Status": text[2]
        }

json_formatted = (json.dumps(
    content_dict,
    sort_keys=True,
    indent=4,
    separators=(',', ': ')
))

if os.path.isfile("expo_data.json"):
    src = "expo_data.json"
    dst = "expo_data.old.json"
    shutil.copyfile(src, dst)

with open("expo_data.json", "w+") as outfile:
    # json.dump(content_dict, outfile)
    outfile.write(json_formatted)


driver.close()
driver.quit()