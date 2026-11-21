
from selenium import webdriver
import time

# Step 1: Launch Chrome
driver = webdriver.Chrome()

# Step 2: Open first website
driver.get("https://www.google.com")
time.sleep(2)

# Step 3: Open second website
driver.get("https://www.wikipedia.org")
time.sleep(2)

# Step 4: Open third website
driver.get("https://www.python.org")
time.sleep(2)

# Step 5: Go back twice
driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

# Print title after Back operations
print("After going back twice:")
print("Current Page Title:", driver.title)

# Step 6: Go forward once
driver.forward()
time.sleep(2)

# Print title after Forward operation
print("\nAfter going forward once:")
print("Current Page Title:", driver.title)

# Step 7: Close browser
driver.quit()
print("\nBrowser closed successfully.")
