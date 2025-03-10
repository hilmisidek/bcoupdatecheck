# bcoupdatecheck

## Description
This repository contains a script designed to check updates on stock and price for BCO dropshippers. It offers an executable file (bco.exe) along with the necessary files to ensure it runs smoothly. Additionally, it includes the Python source code for those who prefer to use the script directly.

## Features
- **Stock and Price Updates:** Monitors stock and price updates for BCO products.
- **Executable File:** Easy to run executable (bco.exe) for quick setup.
- **Python Source Code:** Access to the script for customization and troubleshooting.
- **Output File:** Generates an output file (output281121.xlsx) with the updates.

## Requirements
To use this script, you need the following:
- Python
- Selenium
- Pandas
- Openpyxl
- Chrome WebDriver (ensure it’s the latest version)

## Setup Instructions
1. Clone the repository to your local machine using `git clone [repository URL]`.
2. Place all related files (bco.exe, init.xlsx, cred.txt, chromedriver.exe) in the same directory.
3. If the executable file fails to run, use the Python source code (`bco.py`) and follow the instructions below.
4. Edit `init.xlsx` to include each product URL.
5. Add your username and password to `cred.txt` (1st line: username, 2nd line: password).
6. Run the script and check the output file (output281121.xlsx) for updates.

## Troubleshooting
- If you encounter a “no such element” error during the login phase, comment out line 40 of the script.
- This script is tested working on Windows 10 with Chrome 97. However, it may give errors on Chrome version 96 due to automatic login without clicking the login button.
