
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open a webpage containing an HTML table
driver.get("https://www.w3schools.com/html/html_tables.asp")

# Locate 2nd td inside 3rd tr using XPath
cell = driver.find_element(
    By.XPATH,
    "//table[@id='customers']//tr[3]/td[2]"
)

# Print the cell text
print("Located Table Cell Text:", cell.text)

# Close browser
driver.quit()
