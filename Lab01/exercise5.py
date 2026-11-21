
from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")
time.sleep(2)

# Store title before refresh
title_before = driver.title
print("Title Before Refresh:", title_before)

# Refresh the webpage
driver.refresh()
time.sleep(2)

# Store title after refresh
title_after = driver.title
print("Title After Refresh:", title_after)

# Compare both titles
if title_before == title_after:
    print("Both titles are same.")
else:
    print("Titles are different.")

# Close browser
driver.quit()
print("Browser closed successfully.")
