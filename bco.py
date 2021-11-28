# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:47:54 2021

@author: mij_a
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date


stokCount = pd.Series([],dtype=pd.StringDtype()) #initialize panda series
priceCatch = pd.Series([],dtype=pd.StringDtype())
#read excel file put into data object
data = pd.read_excel (r'D:\pythone selenium\init.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'

df = pd.DataFrame(data) #put into dataframe
df_array=df['url'].values.tolist() #read column url put into array
                  #stok=[1,2]

cred=[]

with open('cred.txt') as f: #this is where you put your username and password (same dir)
    cred = f.readlines() #read line by line, put into list of string

f.close() #close the file
print (f"user: {cred[0]}pass: {cred[1]}") #make sure it is correct. can comment


browser = webdriver.Chrome() #using chrome
browser.minimize_window() 
browser.get('https://bco.com.my') # the url
clickSign=browser.find_element(By.LINK_TEXT,"Sign In")
clickSign.click()
formUsr=browser.find_element(By.ID,"login_main_login")
formUsr.send_keys(cred[0])
formPass=browser.find_element(By.ID,"psw_main_login")
formPass.send_keys(cred[1])
browser.find_element(By.CSS_SELECTOR,".buttons-container:nth-child(5) .ty-btn__login").click()
#addUrl=["https://bco.com.my/150-ungkapan-mudah-bahasa-mandarin/","https://bco.com.my/the-richest-man-in-babylon/"]
#f=open("scrape.txt","a+")
count=0
for address in df_array: #check url one by one 
    browser.get(address)
    harga=browser.find_element(By.XPATH,"//span[2]/span/bdi/span[2]").text
    stok=browser.find_element(By.XPATH,"//div[starts-with(@id,'product_amount_update_')]").text
    stok_split=stok.split(":",2) #split ready stock: xxxx
    stok_split_after_split=stok_split[1].split(" ",2) #split xx pieces
    stok_before_final=stok_split_after_split[0].lstrip("\n") #it capture \n just remove it
    stok_final=stok_before_final #just to make it work
    stokCount[count]=stok_final    #update stock item by item
    priceCatch[count]=harga
    count+=1 #identifier
 #   print ("Title:")
    print (browser.title)
    print ("Price:")
    print (harga)
    print ("Stock:")
    print (stok_final)
data.insert(1, "stok", stokCount) #insert into dataframe column 1 start from 0 eh
data.insert(2, "harga", priceCatch) #insert into dataframe column 2
dateNow=date.today() #get date for today
dateStr=dateNow.strftime("%d%m%y") #convert into string with formatting
outputfile="output" + dateStr +".xlsx" #filename final, don't forget .xslx
print(outputfile) #to make sure filename is good, can remove
data.to_excel(outputfile, index=False) #write to excel file
print (data) # to display final dataset