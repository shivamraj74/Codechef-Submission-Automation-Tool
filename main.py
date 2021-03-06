#first install selenium using - "!pip install selenium"  in console

#then install webdriver, by clicking - hhtp://selenium-python.readthedocs.io/installation.html#drivers
from selenium import webdriver
import getpass
import time

# codechef credentials for login
username = "shivamraj74"
password = getpass.getpass("Password: ")

# problem code
problem = input("Problem code: ")

# submission code
submission_file = input("Submission file: ")

with open(submission_file, 'r') as f:
	code = f.read()

# start a browser session
# can be Chrome too
browser = webdriver.Firefox()

# open link in browser
browser.get('https://www.codechef.com')

# login
nameElem = browser.find_element_by_id('edit-name')
nameElem.send_keys(username)

passElem = browser.find_element_by_id('edit-pass')
passElem.send_keys(password)

browser.find_element_by_id('edit-submit').click()

# open submission page
browser.get("https://www.codechef.com/submit/" + problem)

# sleep function to let web components load in case of slow internet connnection
time.sleep(10)

# click on toggle button to open simple text mode
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

# submit the code
inputElem = browser.find_element_by_id('edit-program')
inputElem.send_keys(code)
# change language to c++

browser.find_element_by_xpath('//*[@id="edit-language"]/option[2]').click()


browser.find_element_by_id("edit-submit").click()

# get result
result = browser.find_element_by_id("display_result").text

print(result)
