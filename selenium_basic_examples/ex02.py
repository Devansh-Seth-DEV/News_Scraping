from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path = "./drivers/geckodriver",
                 log_path = "./logs/geckodriver.log"
                 );
browser = webdriver.Firefox(service=service);

browser.get("https://www.random.org/strings/?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new");
assert "String Generator" in browser.title;

dataElement = browser.find_element(By.CSS_SELECTOR, "pre.data");

print("Random String: %s"% dataElement.text);

browser.close();
