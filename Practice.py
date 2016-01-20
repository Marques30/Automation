from selenium import webdriver

print('Input your codeacademy email address')
userEmail = input()
print('Input your codeacademy password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('http://codeacademy.com')

loginElem = browser.find_element_by_link_text('LOG IN')
loginElem.click()

emailElem = browser.find_element_by_id('user_login')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('user_password')
passwordElem.send_keys(userPassword)
passwordElem.submit()