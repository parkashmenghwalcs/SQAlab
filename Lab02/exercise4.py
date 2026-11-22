
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open login page
driver.get("https://www.saucedemo.com/")

# Locate username using ID
username1 = driver.find_element(By.ID, "user-name")
print("Username found using ID")

# Locate username using NAME
username2 = driver.find_element(By.NAME, "user-name")
print("Username found using NAME")

# Locate username using CSS Selector
username3 = driver.find_element(By.CSS_SELECTOR, "#user-name")
print("Username found using CSS Selector")

# Close browser
driver.quit()
