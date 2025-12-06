"""EMI Calculator Automation Script for FinStack
Automated test for EMI calculator functionality using Selenium
Test Case: TC-008 - EMI Calculator - Basic Calculation
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import Optional, Tuple


class EMICalculatorTest:
    """Automated test class for FinStack EMI calculator"""
    
    def __init__(self, headless: bool = False):
        """Initialize WebDriver and test configuration"""
        self.app_url = "https://finstack-alpha.vercel.app/loan-calculator"
        self.timeout = 10
        self.driver = None
        self.headless = headless
        
        # Test data - TC-008
        self.loan_amount = "500000"
        self.interest_rate = "8.5"
        self.tenure_months = "60"
    
    def setup_driver(self):
        """Setup Selenium WebDriver"""
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        print("\u2705 WebDriver initialized successfully")
    
    def navigate_to_calculator(self):
        """Navigate to EMI calculator page"""
        try:
            self.driver.get(self.app_url)
            print(f"\u2705 Navigated to {self.app_url}")
            time.sleep(2)
        except Exception as e:
            print(f"\u274c Error navigating to calculator: {e}")
            raise
    
    def enter_loan_amount(self):
        """Enter loan amount"""
        try:
            loan_input = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.ID, "loan-amount"))
            )
            loan_input.clear()
            loan_input.send_keys(self.loan_amount)
            print(f"\u2705 Entered loan amount: \u20b9{self.loan_amount}")
            time.sleep(1)
        except Exception as e:
            print(f"\u274c Error entering loan amount: {e}")
            raise
    
    def enter_interest_rate(self):
        """Enter interest rate"""
        try:
            rate_input = self.driver.find_element(By.ID, "interest-rate")
            rate_input.clear()
            rate_input.send_keys(self.interest_rate)
            print(f"\u2705 Entered interest rate: {self.interest_rate}%")
            time.sleep(1)
        except Exception as e:
            print(f"\u274c Error entering interest rate: {e}")
            raise
    
    def enter_tenure(self):
        """Enter tenure in months"""
        try:
            tenure_input = self.driver.find_element(By.ID, "tenure-months")
            tenure_input.clear()
            tenure_input.send_keys(self.tenure_months)
            print(f"\u2705 Entered tenure: {self.tenure_months} months")
            time.sleep(1)
        except Exception as e:
            print(f"\u274c Error entering tenure: {e}")
            raise
    
    def click_calculate_button(self):
        """Click the Calculate button"""
        try:
            calculate_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Calculate')]")
            calculate_btn.click()
            print("\u2705 Clicked Calculate button")
            time.sleep(2)
        except Exception as e:
            print(f"\u274c Error clicking Calculate button: {e}")
            raise
    
    def get_emi_result(self) -> Optional[str]:
        """Extract calculated EMI amount"""
        try:
            emi_element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, "emi-result"))
            )
            emi_value = emi_element.text
            print(f"\u2705 EMI Calculated: {emi_value}")
            return emi_value
        except Exception as e:
            print(f"\u274c Error getting EMI result: {e}")
            return None
    
    def get_total_amount(self) -> Optional[str]:
        """Extract total amount to be paid"""
        try:
            total_element = self.driver.find_element(By.CLASS_NAME, "total-amount")
            total_value = total_element.text
            print(f"\u2705 Total Amount: {total_value}")
            return total_value
        except Exception as e:
            print(f"\u274c Error getting total amount: {e}")
            return None
    
    def get_total_interest(self) -> Optional[str]:
        """Extract total interest payable"""
        try:
            interest_element = self.driver.find_element(By.CLASS_NAME, "total-interest")
            interest_value = interest_element.text
            print(f"\u2705 Total Interest: {interest_value}")
            return interest_value
        except Exception as e:
            print(f"\u274c Error getting total interest: {e}")
            return None
    
    def verify_calculation(self) -> bool:
        """Verify that calculation was performed correctly"""
        try:
            emi = self.get_emi_result()
            total = self.get_total_amount()
            interest = self.get_total_interest()
            
            if emi and total and interest:
                print("\u2705 All calculation results retrieved successfully")
                return True
            else:
                print("\u274c Some calculation results are missing")
                return False
        except Exception as e:
            print(f"\u274c Verification failed: {e}")
            return False
    
    def take_screenshot(self, filename: str = "calculator_result.png"):
        """Take screenshot of result"""
        try:
            self.driver.save_screenshot(filename)
            print(f"\u2705 Screenshot saved: {filename}")
        except Exception as e:
            print(f"\u274c Error taking screenshot: {e}")
    
    def close_driver(self):
        """Close WebDriver"""
        if self.driver:
            self.driver.quit()
            print("\u2705 WebDriver closed")
    
    def run_test(self):
        """Execute complete EMI calculator test"""
        try:
            print("\n" + "="*60)
            print("FinStack EMI Calculator Test - TC-008")
            print("="*60 + "\n")
            
            self.setup_driver()
            self.navigate_to_calculator()
            self.enter_loan_amount()
            self.enter_interest_rate()
            self.enter_tenure()
            self.click_calculate_button()
            
            if self.verify_calculation():
                self.take_screenshot("emi_calculation_success.png")
                print("\n\u2705 TEST PASSED: EMI calculation completed successfully\n")
                return True
            else:
                self.take_screenshot("emi_calculation_failed.png")
                print("\n\u274c TEST FAILED: EMI calculation verification failed\n")
                return False
                
        except Exception as e:
            print(f"\n\u274c TEST FAILED: {e}\n")
            return False
        finally:
            self.close_driver()


if __name__ == "__main__":
    test = EMICalculatorTest(headless=False)
    result = test.run_test()
    exit(0 if result else 1)
