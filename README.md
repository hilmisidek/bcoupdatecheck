# bcoupdatecheck
check updates on stock and price for bco dropshipper

02-Dec-2021 : 
EXE file created. You can try to run the file but be sure to put all related files in the same directory

1. bco.exe
2. init.xlsx
3. cred.txt
4. chromedriver.exe (always check for latest driver)

If cannot run, use the python source code and read below:

This script is tested working on windows 10 machine

To use this script you need:
1. Python
2. Selenium
3. Pandas
4. Openpyxl
5. webdriver (in this case chrome)

init.xlsx is where you put each product url

cred.txt is where you put your username and password (1st line: username, 2nd line: password). 

output281121.xlsx is the output of the updates

bco.pcy is the script

I don't know how to get this script into executable, used py-to-exe but it was failed. 

In case no such element erro occured on login phase. comment line 40. 
Working fne on chrome 97 but seems giving this error on version 96. Seems like after inserting password it
get logged on automatically without clicking on the login button
