# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:47:54 2021

@author: hilmisidek@hotmail.com
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date


def credential():
    credFetch = []  # intialize cred array to stor credential
    with open('cred.txt') as f:  # this is where you put your username and password (same dir)
        credFetch = f.readlines()  # read line by line, put into list of string
    f.close()  # close the file
    print(f"user: {credFetch[0]}pass: {credFetch[1]}")  # make sure it is correct. can comment
    return credFetch


def login_main(browser):
    browser.minimize_window()
    browser.get('https://bco.com.my')  # the url
    clickSign = browser.find_element(By.LINK_TEXT, "Sign In")
    clickSign.click()
    formUsr = browser.find_element(By.ID, "login_main_login")
    cred = credential()
    formUsr.send_keys(cred[0])
    formPass = browser.find_element(By.ID, "psw_main_login")
    formPass.send_keys(cred[1])



def file_naming():
    dateNow = date.today()  # get date for today
    dateStr = dateNow.strftime("%d%m%y")  # convert into string with formatting
    outputfile = "output" + dateStr + ".xlsx"  # filename final, don't forget .xslx
    print(outputfile)  # to make sure filename is good, can remove
    return outputfile


def get_stock(stok):
    stok_split = stok.split(":", 2)  # split ready stock: xxxx pieces
    stok_split_after_split = stok_split[1].split(" ", 2)  # split xx pieces
    stok_before_final = stok_split_after_split[0].lstrip("\n")  # it capture \n just remove it
    stok_final = stok_before_final  # just to make it work
    return stok_final


def pre_process(data):
    df = pd.DataFrame(data)  # put into dataframe
    df_array = df['url'].values.tolist()  # read column url put into array
    return df_array


def post_process (data, stokCount, priceCatch):
    data.insert(1, "stok", stokCount)  # insert into dataframe column 1 start from 0 eh
    data.insert(2, "harga", priceCatch)  # insert into dataframe column 2
    data.to_excel(file_naming(), index=False)  # write to excel file
    print(data)  # to display final dataset


def main():
    browser = webdriver.Chrome()  # using chrome
    data = pd.read_excel(r'init.xlsx')  # place "r" before the path string to address special character, such as '\'.
    stokCount = pd.Series([], dtype=pd.StringDtype())  # initialize panda series
    priceCatch = pd.Series([], dtype=pd.StringDtype())
    df_array=pre_process(data)
    count = 0

    login_main(browser)

    for address in df_array:  # check url one by one
        try:
            browser.get(address)
            harga = browser.find_element(By.XPATH, "//span[starts-with(@id,'sec_discounted_price_')]").text
            stok = browser.find_element(By.XPATH, "//div[starts-with(@id,'product_amount_update_')]").text
            stok_final=get_stock(stok)
            stokCount[count] = stok_final  # update stock item by item
            priceCatch[count] = harga
            print(browser.title)
            print("Price:")
            print(harga)
            print("Stock:")
            print(stok_final)
        except Exception as e:
            print(f"URL {address} got problem")  # tell the error
            stokCount[count] = "check"
            priceCatch[count] = "check"
            print(e)
        finally:
            count += 1
    post_process(data, stokCount, priceCatch)


if __name__ == "__main__":
    main()
