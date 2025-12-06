"""Login Automation Script for FinStack
Automated test for login functionality using Selenium WebDriver
Test Case: TC-001 - Login with Valid Credentials
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
from typing import Optional


class FinStackLoginTest:
    """Automated test class for FinStack login functionality"""
    
    def __init__(self, headless: bool = False):
        """Initialize WebDriver and test configuration"""
        self.app_url = "https://finstack-alpha.vercel.app/login"
        self.username = "testuser@finstack.com"
        self.password = "TestPassword123"
        self.timeout = 10
        self.driver = None
        self.headless = headless
    
    def setup_driver(self):
        """Setup Selenium WebDriver"""
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        print("\u2705 WebDriver initialized successfully")
    
    def navigate_to_login(self):
        """Navigate to login page"""
        try:
            self.driver.get(self.app_url)
            print(f"\u2705 Navigated to {self.app_url}")
            time.sleep(2)
        except Exception as e:
            print(f"\u274c Error navigating to login page: {e}")
            raise
    
    def enter_credentials(self):
        """Enter username and password"""
        try:
            # Find and enter username
            username_field = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(self.username)
            print(f"\u2705 Entered username: {self.username}")
            
            # Find and enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(self.password)
            print(f"\u2705 Entered password (****)")
            
        except Exception as e:
            print(f"\u274c Error entering credentials: {e}")
            raise
    
    def click_login_button(self):
        """Click the login button"""
        try:
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            print("\u2705 Clicked login button")
            time.sleep(2)
        except Exception as e:
            print(f"\u274c Error clicking login button: {e}")
            raise
    
    def verify_login_success(self) -> bool:
        """Verify that login was successful"""
        try:
            # Wait for dashboard to load (URL should change or dashboard element visible)
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
            )
            current_url = self.driver.current_url
            print(f"\u2705 Login successful! Current URL: {current_url}")
            return True
        except Exception as e:
            print(f"\u274c Login verification failed: {e}")
            return False
    
    def get_balance(self) -> Optional[str]:
        """Extract account balance from dashboard"""
        try:
            balance_element = self.driver.find_element(By.CLASS_NAME, "account-balance")
            balance = balance_element.text
            print(f"\u2705 Account Balance: {balance}")
            return balance
        except Exception as e:
            print(f"\u274c Error getting balance: {e}")
            return None
    
    def take_screenshot(self, filename: str = "screenshot.png"):
        """Take a screenshot of current page"""
        try:
            self.driver.save_screenshot(filename)
            print(f"\u2705 Screenshot saved: {filename}")
        except Exception as e:
            print(f"\u274c Error taking screenshot: {e}")
    
    def close_driver(self):
        """Close WebDriver and cleanup"""
        if self.driver:
            self.driver.quit()
            print("\u2705 WebDriver closed")
    
    def run_test(self):
        """Execute complete login test"""
        try:
            print("\n" + "="*60)
            print("FinStack Login Automation Test - TC-001")
            print("="*60 + "\n")
            
            self.setup_driver()
            self.navigate_to_login()
            self.enter_credentials()
            self.click_login_button()
            
            if self.verify_login_success():
                self.get_balance()
                self.take_screenshot("login_success.png")
                print("\n\u2705 TEST PASSED: Login was successful\n")
                return True
            else:
                self.take_screenshot("login_failed.png")
                print("\n\u274c TEST FAILED: Login verification failed\n")
                return False
                
        except Exception as e:
            print(f"\n\u274c TEST FAILED: {e}\n")
            return False
        finally:
            self.close_driver()


if __name__ == "__main__":
    test = FinStackLoginTest(headless=False)
    result = test.run_test()
    exit(0 if result else 1)
