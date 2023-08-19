from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from gtts import gTTS
from datetime import datetime
import os

def FirefoxInit(binaryPath: str, logFilePath: str) -> webdriver.firefox.webdriver.WebDriver:
    service = Service(
            executable_path = binaryPath,
            log_path = logFilePath
            )
    driver = webdriver.Firefox(service=service);
    return driver;

def OpenSite(driver: webdriver.firefox.webdriver.WebDriver, site: str="https://www.google.com", waitSec: int=0.8) -> None:
    driver.implicitly_wait(waitSec);
    driver.get(site);

def LocateElement(element: webdriver.remote.webelement.WebElement, locator: str, value: str) -> webdriver.remote.webelement.WebElement:
    webElement = element.find_element(locator, value);
    return webElement;

def LocateElements(element: webdriver.remote.webelement.WebElement, locator: str, value: str) -> list[webdriver.remote.webelement.WebElement]:
    webElements = element.find_elements(locator, value);
    return webElements;

def LocateElementFromDriver(driver: webdriver.firefox.webdriver.WebDriver, locator: str, value: str) -> webdriver.remote.webelement.WebElement:
    webElement = driver.find_element(locator, value);
    return webElement;

def LocateElementsFromDriver(driver: webdriver.firefox.webdriver.WebDriver, locator: str, value: str) -> list[webdriver.remote.webelement.WebElement]:
    webElements = driver.find_elements(locator, value);
    return webElements;

def CloseDriver(driver: webdriver.firefox.webdriver.WebDriver) -> None:
    driver.close();
    driver.quit();

def StoreHeadlines(filePath: str, fileName: str, headlines: list[webdriver.remote.webelement.WebElement]) -> None:
    currentDateTime = datetime.now();
    if(filePath[-1] != '/'):
        filePath += '/';

    try:
        file = open("%s%s[%s].txt"%(filePath, fileName, currentDateTime), "w");
        for element in headlines:
            file.write("%s\n"%element.text);
        file.close();
        print("Saved file: %s%s[%s].txt"%(filePath, fileName, currentDateTime));
    except Exception as error:
        print("error occured while generating text file");
        print("ERROR: %s"%error);

def GoogleTTS(textsToSpeech: list[webdriver.remote.webdriver.WebDriver], lang: str, audioName: str, sourceDir: str) -> None:
    if(sourceDir[-1] != '/'):
        sourceDir += "/";

    currentDateTime = datetime.now();
    sourceDir +=  "%s/"%currentDateTime;

    try:
        if not os.path.exists(sourceDir):
            os.makedirs(sourceDir);
            print("Created Directory: %s[current headlines audio directory]" %sourceDir);
            print();
    except FileExistsError:
        pass

    for i, element in enumerate(textsToSpeech):
        try:
            print("Converting headline %d to %s%d.mp3..."%(i+1, audioName, i+1));
            tts = gTTS("%s"%element.text, lang=lang);
            tts.save("%s%s%d.mp3"%(sourceDir, audioName, i+1));
            print("Saved: %s%d.mp3"%(audioName, i+1));
            print();
        except Exception as error:
            print("unable to convert into audio file");
            print("ERROR: %s"%error);
            print();

def PrintNewsHeadlines(title: str="", headlines: list[webdriver.remote.webelement.WebElement]=[]) -> None:
    print("%s"%title);
    print("="*20);
    for i, element in enumerate(headlines):
        print();
        print("HEADLINE [%d]: %s"%(i+1, element.text));
        print("_"*10);

if __name__ == "__main__":
    NEWS_SITE: str = "https://www.hindustantimes.com/";
    HEADLINES_DIR: str = "./docs/headlines/"
    CAPTURE_FILENAME: str = "Headlines";
    DRIVER_PATH: str = "./drivers/FirefoxDriver/geckodriver";
    LOGFILES_PATH: str = "./logs/geckodriver.log";
    AUDIODIR_PATH: str = "./audio/"

    print("Running firefox driver...");
    driver = FirefoxInit(DRIVER_PATH, LOGFILES_PATH);

    print("Opening %s"%NEWS_SITE);
    OpenSite(driver, NEWS_SITE);

    newsContainer = LocateElementFromDriver(driver, By.ID, "topnews");
    headLinesContainer = LocateElement(newsContainer, By.CLASS_NAME, "htImpressionTracking");
    headlines = LocateElements(headLinesContainer, By.CSS_SELECTOR, "h3.hdg3");

    print();
    PrintNewsHeadlines("TOP HEADLINES", headlines);

    print("\nGenerating text file of headlines...");
    StoreHeadlines(HEADLINES_DIR, CAPTURE_FILENAME, headlines);

    print("\nInitiating Process: Text-To-Speech Converstion");
    GoogleTTS(headlines, "en", "headline", AUDIODIR_PATH);

    print("\nClosing the firefox driver and calls ...");
    CloseDriver(driver);
    exit();
