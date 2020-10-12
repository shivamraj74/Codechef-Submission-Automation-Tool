#first install selenium using - "!pip install selenium"  in console

#then install webdriver, by clicking - hhtp://selenium-python.readthedocs.io/installation.html#drivers
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#open empty window
browser = webdriver.Chrome(ChromeDriverManager().install())

#open particular url
browser.get("https://codechef.com")

#after checking the ids of what we need to fill
username_element=browser.find_element_by_id("edit-name")

#send your username
username_element.send_keys("shivamraj74")

#now do same for password element 
password_element=browser.find_element_by_id("edit-pass")

password_element.send_keys("type_your_password _here") #or use below 2 lines of code to manually enter password
#for not showing password
#from getpass import getpass
#password_element.send_keys(getpass("enter password"))

#find submit button and click that
browser.find_element_by_id("edit-submit").click()

browser.get("https://www.codechef.com/submit/questionCode")  #codechef problem link here

#clicking the togle editor everytime we visit
#browser.find_element_by_id('edit_area_toggle_checkbox_edit-program').click()

#opening and reading solution to be submitted
with open("Solution.cpp",'r') as f:   #code file here
    code=f.read()

#writing this code in text area on codechef 

code_element=browser.find_element_by_id("edit-program")

code_element.send_keys(code)

#clicking on submit button to submit code
import time
time.sleep(10)
browser.find_element_by_id("edit-submit-1").click()   
