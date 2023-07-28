from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

def FirefoxInit(binaryPath: str, logFilePath: str) -> webdriver.firefox.webdriver.WebDriver:
    service = Service(
            executable_path = binaryPath,
            log_path = logFilePath
            )
    driver = webdriver.Firefox(service=service);
    return driver;

def OpenSite(driver: webdriver.firefox.webdriver.WebDriver, site: str="https://www.google.com", waitSec: int=0.5) -> None:
    driver.get(site);
    driver.implicitly_wait(waitSec);

def LocateElement(element: webdriver.remote.webelement.WebElement, locator: str, value: str) -> webdriver.remote.webelement.WebElement:
    webElement = element.find_element(locator, value);
    return webElement;

def LocateElements(element: webdriver.remote.webelement.WebElement, locator: str, value: str) -> list:
    webElements = element.find_elements(locator, value);
    return webElements;

def LocateElementFromDriver(driver: webdriver.firefox.webdriver.WebDriver, locator: str, value: str) -> webdriver.remote.webelement.WebElement:
    webElement = driver.find_element(locator, value);
    return webElement;

def LocateElementsFromDriver(driver: webdriver.firefox.webdriver.WebDriver, locator: str, value: str) -> list:
    webElements = driver.find_elements(locator, value);
    return webElements;

def CloseDriver(driver: webdriver.firefox.webdriver.WebDriver) -> None:
    driver.close();
    driver.quit();

def PrintNewsHeadlines(title: str="", headlines: list=[]) -> None:
    print("%s"%title);
    print("="*20);
    for i, element in enumerate(headlines):
        print();
        print("HEADLINE [%d]: %s"%(i+1, element.text));
        print("_"*10);

def StoreHeadlines(filePath: str, headlines: list) -> None:
    file = open(filePath, "w+");
    for element in headlines:
        file.write("%s\n"%element.text);
    file.close();

if __name__ == "__main__":
    NEWS_SITE: str = "https://www.hindustantimes.com/";

    driver = FirefoxInit("./driver/geckodriver", "./logs/geckodriver.log");

    OpenSite(driver, NEWS_SITE);

    newsContainer = LocateElementFromDriver(driver, By.ID, "topnews");

    headLinesContainer = LocateElement(newsContainer, By.CLASS_NAME, "htImpressionTracking");

    headlines = LocateElements(headLinesContainer, By.CSS_SELECTOR, "h3.hdg3");

    PrintNewsHeadlines("TOP HEADLINES", headlines);

    StoreHeadlines("./news_scraping/headlines.txt", headlines);
    CloseDriver(driver);
