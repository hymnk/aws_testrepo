import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import chromedriver_binary

# 
url = 'https://signin.aws.amazon.com/console'
username = ''
password = ''
service_name = '請求'

#
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}
resp = requests.get(url, timeout=1, headers=headers, verify=False)
encoding = resp.encoding
print(encoding)

options = Options()
#options.add_argument('--headless')

# chrome起動、ログインページへアクセス
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)
driver.set_page_load_timeout(30)
driver.get(url)

# ログイン処理
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_id('signin_button').click()

# 請求情報へ移動
search_box = driver.find_element_by_id('search-box-input')
search_box.send_keys(service_name)
search_box.send_keys(Keys.ENTER)

#driver.find_element_by_class_name('navLink--1isy-').click()
driver.find_element_by_xpath('//*[@id="billing-console-root"]/div/div/div[2]/div/div/div/div/awsui-column-layout/div/span/div/div[2]/div/div[1]/div[1]/awsui-button').click()
# driver.find_element_by_class_name('awsui-expandable-section-header').click()
# driver.find_element_by_class_name('product-details-by-region').click()
driver.find_element_by_xpath('//*[@id="bills-page-antelope"]/div[5]/div/div/div/div[1]/div[1]/awsui-button/button').click()

print(driver.page_source)

# element_list = driver.find_elements_by_tag_name('div')
# for elem in element_list:
#     print(elem)

time.sleep(10)

driver.close()
driver.quit()
