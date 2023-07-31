![Web Scraping](https://cdn.filestackcontent.com/m8n7GlrdTBChzowoPeFp)

# News Reader-Selenium Project

Web scraping is the automated gathering of content and data from a website or any other resource available on the internet. 
Unlike screen scraping, web scraping extracts the HTML code under the webpage. 
Users can then process the HTML code of the webpage to extract data and carry out data cleaning, manipulation, and analysis
<br>

### Project Description:
In this project , Web Browser will be accessed with Selenium. News has to be fetched from the browser & printed [ from the specifiesource eg- Hindustan Times ],
then converting the news text into speech & saving it into audio file

Designed for [Linux](https://www.linux.org/). *Not yet tested on [Windows](https://www.microsoft.com/en-in) and [macOS!](https://support.apple.com/en-in/macos)*
<br><br>

Installation
---
STEP1: Clone this repository by
`git clone https://github.com/Devansh-Seth-DEV/News_Scraping.git`

STEP2: Create a virtual environment by <br>
> Open your favourite Terminnal
```
~$ cd <path to cloned repository> ...
News_Scraping:~$ pip3 install virtualenv
News_Scraping:~$ virtualenv venv_name
```

STEP3: Activate virtual environment
```
News_Scraping:~$ source venv_name/bin/activate
```

STEP4: Give permissions to firefox driver
```
(venv_name) News_Scraping:~$ chmod +x drivers/FirefoxDriver/geckodriver
```

Install Selenium and gTTS (Google-Text-To-Speech)
---
> Assuming that the virtual environment is activated
```
(venv_name) News_Scraping:~$ pip3 install selenium
(venv_name) News_Scraping:~$ pip3 install webdriver-manager
(venv_name) News_Scraping:~$ pip3 install gTTS
```

RUN
---
> Assuming that the virtual environment is activated <br>
```
(venv_name) News_Scraping:~$ python3 news_scraperBOT.py
```

OUTPUT
---
News Text-Files Directory
```
(venv_name) News_Scraping:~$ cd ./docs/headlines
```
News-Text Audio Directory: 
```
(venv_name) News_Scraping:~$ cd ./audio/
```

Deactivating Virtual Environment
---
```
(venv_name) News_Scraping:~$ deactivate
```
