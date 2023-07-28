from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(executable_path = "./drivers/geckodriver",
                  log_path = "./logs/geckodriver.log"
                  );

browser = webdriver.Firefox(service=service);
browser.get("http://random-name-generator.info/");

nameList = browser.find_elements(By.CSS_SELECTOR, "ol.nameList li");

print("NAME LIST: ");
for name in nameList:
    print("%s"%name.text);

browser.close();
