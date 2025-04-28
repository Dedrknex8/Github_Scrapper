from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

repo = input(" Enter the gituhb username you want to target : ")

if not repo.startswith("https://github.com/"):
    repo =  "https://github.com/" + repo
service = Service(ChromeDriverManager().install()) # Install Chrome driver automatiically to version of chrome installed
driver = webdriver.Chrome(service=service)


driver.get(repo)
res = driver.find_elements(By.CLASS_NAME, "repo")

for elements in res:
    print(elements.text)

driver.quit()