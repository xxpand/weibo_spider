from selenium import webdriver
from selenium.webdriver import ActionChains
import time

accounts = list()
with open('Account', 'r') as f:
    for account in f.readlines():
        accounts.append(account)


def login():
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    username = accounts[0].split(':')[0]
    password = accounts[0].split(':')[1]
    print(username, password)
    driver.get('http://weibo.cn')
    driver.implicitly_wait(5)
    login_link = driver.find_element_by_link_text('登录')
    ActionChains(driver).move_to_element(login_link).click().perform()
    login_name = driver.find_elements_by_id("loginName")[0]
    login_password = driver.find_element_by_id("loginPassword")
    login_name.send_keys(username)
    login_password.send_keys(password)
    login_button = driver.find_element_by_id("loginAction")
    login_button.click()
    time.sleep(1)
    cookie = driver.get_cookies()

    cookie_dic = dict()
    for cookieitem in cookie:
        if 'name' in cookieitem and 'value' in cookieitem:
            cookie_dic[cookieitem['name']] = cookieitem['value']
    del accounts[0]
    print(cookie_dic)
    return cookie_dic
