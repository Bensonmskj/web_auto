#!/usr/bin/python3
import os
from selenium import webdriver
from time import sleep

file_path = os.path.abspath('')
print("file_path:",file_path)
driver = webdriver.Chrome()
upload_page = 'file:///' + file_path + '/upload_file.html'
driver.get(upload_page)

#定位上传按钮，添加本地文件
#driver.find_element_by_name("file").click()
driver.find_element_by_name("file").send_keys(file_path + '/test.txt')



