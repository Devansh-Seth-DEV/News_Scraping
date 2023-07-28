from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path="./drivers/geckodriver",
        log_path="./logs/geckodriver.log"
        );
browser = webdriver.Firefox(service=service);
browser.get("http://www.google.com");
print("Title: %s"% browser.title);
sleep(5);
browser.quit();
