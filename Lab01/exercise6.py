
from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open first website
driver.get("https://www.google.com")
time.sleep(2)

print("First Website:")
print("Title:", driver.title)
print("URL:", driver.current_url)

# Open second website
driver.get("https://www.wikipedia.org")
time.sleep(2)

print("\nSecond Website:")
print("Title:", driver.title)
print("URL:", driver.current_url)

# Go back
driver.back()
time.sleep(2)
print("\nAfter Going Back:")
print("Title:", driver.title)

# Go forward
driver.forward()
time.sleep(2)
print("\nAfter Going Forward:")
print("Title:", driver.title)

# Refresh webpage
driver.refresh()
time.sleep(2)
print("\nAfter Refresh:")
print("Title:", driver.title)

# Close browser
driver.quit()
print("\nBrowser closed successfully.")
