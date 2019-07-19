# -*- coding: utf-8 -*-
# 2019/01/03
# @Author: JeremyZ

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.set_page_load_timeout(10)
driver.set_script_timeout(10)
driver.set_window_size(1366, 768)

driver.get('https://weibo.cn/')
