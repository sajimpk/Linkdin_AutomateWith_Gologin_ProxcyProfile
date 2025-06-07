# linkedin_login.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD

def login_to_linkedinQ(debugger_address):
    print("likdin")
    service = Service(ChromeDriverManager(driver_version="135.0.7049.114").install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.linkedin.com/login")

    try:
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys(LINKEDIN_EMAIL)
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(LINKEDIN_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

   

    # if "checkpoint" in driver.current_url or "challenge" in driver.current_url:
    #     print("[!] OTP/Verification required. Visit http://localhost:5000 to enter OTP manually.")
    #     input("Press Enter after OTP is handled manually...")

    return driver

