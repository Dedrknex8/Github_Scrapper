from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import time

repo = input(" Enter the gituhb username you want to target : ")

if not repo.startswith("https://github.com/"):
    repo =  "https://github.com/" + repo
service = Service(ChromeDriverManager().install()) # Install Chrome driver automatiically to version of chrome installed
driver = webdriver.Chrome(service=service)


driver.get(repo)
res = driver.find_elements(By.CLASS_NAME, "repo")
links = []
final_link = []
def raw(second_page):
    driver.get(second_page)
    get_raw = driver.find_element(By.CLASS_NAME, 'gWqxTd')
    get_raw.click()
    src = driver.page_source
    src = f"{src}"
    
    if "password" in src:
        print(f"password found {second_page}")


def loop(next_page):
    global check
    driver.get(next_page)
    new_link = driver.find_elements(By.CLASS_NAME, 'react-directory-truncate')
    for check in new_link:
        pass
    if "py" in check.text:
        second_page =  f"{next_page}/blob/main/{check.text}"
        print("raw found")
        raw(second_page)
    else:
        print("Could not find any main.py")






for elements in res:
    links.append(elements.text)

for i in links:
    next_page = f"{repo}/{i}"
    final_link.append(next_page)
    loop(next_page)
driver.quit()