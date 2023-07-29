from selenium import webdriver
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import json

chrome_driver_path = "Paste your Chrome Driver here"
# brave_browser_path = '/usr/bin/brave-browser'

headers = {
    "Accept-Language":  "en-US,en;q=0.7",
    "User-Agent":       "Paste your User Agent Here"
}


# For San Francisco
# Form_LINK = "Paste your Form link here"
# ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# For New York
# Form_LINK = "Paste your Form link here"
# ZILLOW_URL = "https://www.zillow.com/ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-83.471456515625%2C%22east%22%3A-68.068624484375%2C%22south%22%3A38.54049902958296%2C%22north%22%3A46.76325434718096%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D"

# For Chicago
# Form_LINK = "Paste your Form link here"
# ZILLOW_URL = "https://www.zillow.com/chicago-il/rentals/?searchQueryState=%7B%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22north%22%3A42.365633002706545%2C%22east%22%3A-86.83964701246268%2C%22south%22%3A41.32215552658866%2C%22west%22%3A-88.76500101636893%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A17426%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%2C%22mapZoom%22%3A9%7D"

# For Washington DC
Form_LINK = "Paste your Form link here"
ZILLOW_URL = "https://www.zillow.com/washington-dc/rentals/?searchQueryState=%7B%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22north%22%3A38.88986180307057%2C%22east%22%3A-76.96865658690372%2C%22south%22%3A38.82168630877222%2C%22west%22%3A-77.08899121214786%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41568%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"


class Zillow_bot:
    def __init__(self, ZILLOW_URL, headers, Form_LINK) -> None:
        self.addresses = []
        self.links = []
        self.prices = []
        self.url = ZILLOW_URL
        self.form = Form_LINK
        self.headers = headers
        chrome_service = Service(executable_path=chrome_driver_path)
        chrome_options = Options()
        # chrome_options.binary_location = brave_browser_path
        self.driver = webdriver.Chrome(
            service=chrome_service, options=chrome_options)

    def get_rental_listing(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        zillow_webpage = response.text

        soup = BeautifulSoup(zillow_webpage, 'html.parser')
        data = soup.find_all("script", type="application/json")

        data2 = data[1].string
        listings1 = json.loads(data2)

        listings = listings1["props"]["pageProps"]["searchPageState"]["cat1"]

        search_list = listings["searchResults"]["listResults"]

        for result in search_list:
            # Constructing adresses list
            try:
                building = result["buildingName"]
                self.addresses += [building+' | '+result["address"]]
            except:
                self.addresses += [result["address"]]
            # Constructing prices list
            try:
                self.prices += [result["units"][0]["price"].strip('+')]
            except:
                self.prices += [result["price"].strip('/mo')]
            # Constructing links list
            main_page = "https://www.zillow.com"
            if main_page in result["detailUrl"]:
                self.links += [result["detailUrl"]]
            else:
                self.links += [main_page + result["detailUrl"]]

    def fill_forms(self):
        self.driver.get(self.form)
        time.sleep(2)

        for listing in range(40):

            time.sleep(1)
            fields = self.driver.find_elements(
                By.CSS_SELECTOR, 'input[type="text"]')

            fields[0].send_keys(self.addresses[listing])
            fields[1].send_keys(self.prices[listing])
            fields[2].send_keys(self.links[listing])

            submit = self.driver.find_element(
                By.CSS_SELECTOR, 'div[role="button"]')
            submit.click()
            time.sleep(2)
            self.driver.get(self.form)


rentalSanFrancisco = Zillow_bot(ZILLOW_URL, headers, Form_LINK)

rentalSanFrancisco.get_rental_listing()
rentalSanFrancisco.fill_forms()
