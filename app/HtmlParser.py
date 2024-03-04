import re
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HtmlParser:

    #ip address to get and read html
    ip: str

    #sovol ui language (only german supported for now)TODO:
    lang: str

    #last checked state of printer
    lastTempCheckValue: bool = True


    """
    init html parser
    ip: ip address of printer
    """
    def __init__(self, ip: str, lang: str):
        self.ip = ip
        if (lang != "DE"):
            raise(f"Unsupported language {lang}.")
        else:
            self.lang = lang


    """
    check if temp is lower than threshold and last threshold was different
    threshold: value to check
    returns true: if lower than threshold
    returns false: if not lower than threshold
    """
    def checkTemp(self, threshold: float) -> bool:

        try:
            temp = HtmlParser.getTempFromHTML(self)
        except Exception as e:
            print(e)
            return False

        #temperature is lower than threshold + last state was higher than threshold
        if temp < threshold and HtmlParser.lastTempCheckValue == False:
            HtmlParser.lastTempCheckValue = True
            return True
        
        #temperature is higher than threshold
        if temp > threshold:
            HtmlParser.lastTempCheckValue = False
            return False
        
        #temperature is lower than threshold but it also was the during the last check
        else:
            return False

    
    """
    checks temperature in html page
    returns temperature
    """
    def getTempFromHTML(self) -> float:
        
        #get html from response
        html = HtmlParser.getHTML(self)
        
        #find first occurance of "°C"
        match = re.search(r'(\d+(?:\.\d+)?)°C', html)

        #check if index could be found
        if not match:
            raise("No value for temperature found. Are you possibly using Fahrenheit instead of Celsius?")
        
        #else continue filtering out the temperature value from the response
        else:
            temp = float(match.group(1))

            print(f"Measured temperature: {temp}")
            return temp
    

    def getHTML(self) -> str:
        #check response returns 200
        response = requests.get(f"http://{self.ip}")
        if (response.status_code == 200):

            #load chrome as headless browser
            chromeOptions = Options()
            chromeOptions.add_argument("--headless")
            chromeOptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
            driver = webdriver.Chrome(options=Options().add_argument("--headless"))

            #load page after executing javascript
            driver.get(f"http://{self.ip}")
            
            #sleep because page needs some time to load data
            time.sleep(10)

            #store html
            html = driver.page_source

            #close chrome
            driver.quit()

            #parse html
            soup = BeautifulSoup(html, 'html.parser')

            return soup.text

        else: 
            raise(f"Error: URL could not be opened.")
