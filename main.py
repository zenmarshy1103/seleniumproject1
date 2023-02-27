from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Boiler plate for initialising webdriver and going to a website 
driver = webdriver.Chrome()
driver.get("https://www.google.com")

#Getting the tiltle of the website ran by the driver
title = driver.title
print("thie is {}".format(title))

#Make the webdriver to wait for the by name variable "q" in the DOM)
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q")))

#Search for the search bar in google.com with the class name of gLFyf
searchBar = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
if searchBar:
    print("Search Bar Found")

#allow the website to be on until a key is pressed in the IDE environment
input("Press enter to quit...")

#shut the web browser that is ran by the webdriver
driver.quit()








