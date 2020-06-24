from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# INITIALIZE THE DRIVER
#

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver" # (or wherever yours is installed)

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)