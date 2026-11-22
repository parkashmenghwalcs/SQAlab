
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome browser
driver = webdriver.Chrome()

# Open Wikipedia
driver.get("https://www.wikipedia.org/")

# Locate all links using TAG_NAME
links = driver.find_elements(By.TAG_NAME, "a")

# Print total links
print("Total links on Wikipedia:", len(links))

# Close browser
driver.quit()
