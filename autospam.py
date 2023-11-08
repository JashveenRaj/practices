from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.service import Service as CommonService
from selenium.webdriver.common.utils import is_connectable
from selenium.webdriver.common import utils

contact = "Jashveen Raj (You)"
text = "automatic message idhu"

# Start a new WebDriver instance
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code
input("Scan QR Code, And then Enter")

# Wait for the user to log in
print("Logged In")

# Locate the search input box and enter the contact name
input_box_search = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
input_box_search.send_keys(contact)
input_box_search.send_keys(Keys.RETURN)

# Locate the chat input box and send the message
input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
input_box.send_keys(text)
input_box.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
