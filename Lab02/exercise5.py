
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open HTML form page
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Find all text input fields using CSS Selector
inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

# Print total matching elements
print("Total text inputs found:", len(inputs))

# Print identifying attributes
for field in inputs:
    print("Input ID:", field.get_attribute("id"))
    print("Input Name:", field.get_attribute("name"))

# Close browser
driver.quit()
