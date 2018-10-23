

# coding:utf-8
import os
import sys
import pandas as pd
import configparser
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

####引数
'''
args = sys.argv
a = args[1]#0は2行目
'''

####ini読み込み
config = configparser.ConfigParser()
config.read(r'C:\Users\jesc1\Dropbox\fril\config.ini', 'UTF-8')
mail = config['account']['mail']
password = config['account']['password']


driver = webdriver.Chrome(r"C:\Users\jesc1\Dropbox\fril\chromedriver.exe")
# ブラウザを開く。
driver.implicitly_wait(10)
driver.get("https://fril.jp/users/sign_in")
driver.find_element_by_id("email").send_keys(mail)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()


# Googleの検索TOP画面を開く。
driver.get("https://fril.jp/item/new")

####セット
a = 0
filename = pd.read_csv(r'C:\Users\jesc1\Dropbox\fril\item.csv')
category1 =filename.iloc[a,0]#
category2 =filename.iloc[a,1]#
category3 =filename.iloc[a,2]#
status =filename.iloc[a,3]#商品の状態
carriage =filename.iloc[a,4]#配送料の負担
delivery_method =filename.iloc[a,4]#配送方法
delivery_date =filename.iloc[a,6]#発送日の目安
delivery_area =filename.iloc[a,7]#発送元の地域
name=filename.iloc[a,8]
detail=filename.iloc[a,9]
sell_price=filename.iloc[a,10]
try:
    img1=filename.iloc[a,11]
except:
    print("画像1はないですね")
try:
    img2=filename.iloc[a,12]
except:
    print("画像2はないですね")
try:
    img3=filename.iloc[a,13]
except:
    print("画像3はないですね")
try:
    img4=filename.iloc[a,14]
except:
    print("画像4はないですね")

#####カテゴリー選択
driver.find_element_by_id("category_name").click()
print("カテゴリー1を選択")
driver.find_element_by_link_text(category1).click()
print("カテゴリー2を選択")
driver.find_element_by_link_text(category2).click()
print("カテゴリー3を選択")
driver.find_element_by_link_text(category3).click()
####商品の状態
driver.find_element_by_id("status").click()
Select(driver.find_element_by_id("status")).select_by_visible_text(status)
####配送料の負担
driver.find_element_by_id("carriage").click()
Select(driver.find_element_by_id("carriage")).select_by_visible_text(carriage)
####配送方法
driver.find_element_by_id("delivery_method").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='スマートレター'])[1]/following::span[2]").click()
####発送日の目安
driver.find_element_by_id("delivery_date").click()
Select(driver.find_element_by_id("delivery_date")).select_by_visible_text(delivery_date)
####発送元の地域
driver.find_element_by_id("delivery_area").click()
Select(driver.find_element_by_id("delivery_area")).select_by_visible_text(delivery_area)
####商品名
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys(name)
####商品説明
driver.find_element_by_id("detail").clear()
driver.find_element_by_id("detail").send_keys(detail)
####商品価格
driver.find_element_by_id("sell_price").clear()
driver.find_element_by_id("sell_price").send_keys(sell_price)
"""
element = driver.find_element_by_xpath("//*[@id='files']/div[1]")
element.send_keys(img1)
element = driver.find_element_by_xpath("//*[@id='files']/div[2]")
element.send_keys(img2)
element = driver.find_element_by_xpath("//*[@id='files']/div[3]")
element.send_keys(img3)
element = driver.find_element_by_xpath("//*[@id='files']/div[4]")
element.send_keys(img4)
"""
try:
    driver.find_element_by_id("image_tmp").send_keys(img1)
except:
    print(a)

try:
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='編集'])[1]/following::input[7]").send_keys(img2)
except:
    print(a)

try:
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='編集'])[2]/following::input[7]").send_keys(img3)
except:
    print(a)

try:
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='編集'])[3]/following::input[7]").send_keys(img4)
except:
    print(a)


driver.find_element_by_id("confirm").click()
