# coding:utf-8

from selenium import webdriver

url = "http://172.16.0.96:8060"
path = '//*[@id="app"]/div/div[3]/div/div[1]/form/div[2]/input'

driver = webdriver.Chrome()
driver.get(url)
attr_ele = driver.find_element_by_xpath(path).get_attribute("type")
# attr = ele.get_attribute("type")

print(attr_ele)

driver.quit()

