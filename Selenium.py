from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# INITIALIZE THE DRIVER
#

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

#
# NAVIGATE TO GOOGLE.COM...
#

driver.get("https://www.bls.gov/news.release/empsit.toc.htm")
print(driver.title) #> BLS Employment Situation
driver.save_screenshot("search_page.png")

#
# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//input[@title="Search"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)

#
# INTERACT WITH THE ELEMENT
#

clickbox_xpath = '//input[@name="Employment Situation Summary"]'
clickbox = driver.find_element_by_xpath(clickbox_xpath)


#element = driver.find_element :xpath, '//input[@name="Employment Situation Summary"]'
#element.click()

# search_term = "Employment Situation Summary"
#first_link = driver.find_element_by_link_text(u'Employment Situation Summary')
#first_link.click()

#click(search_term)
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
print(driver.title) #> 'Employment Situation Summary- BLS Search'
driver.save_screenshot("search_results.png")

#
# ALWAYS QUIT THE DRIVER
#

driver.quit()