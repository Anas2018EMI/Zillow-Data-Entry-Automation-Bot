# Zillow-Data-Entry-Automation-Bot


This bot web scrapes rental listings in Zillow website and saves the data in Google forms. It actually uses Beautiful Soup to web scrape listed appartments for rent in Zillow. Then the bot uses Selenium web driver to fill out a simple form of all the web scraped data in Google Forms. For simplicity reasons, the bot is used in one specific case and the data are saved in Google Forms. However, the code can be tweaked to scale up the web scraping process (different case scenarios, multiple variables, big amount of data...).

But first, you need to create a new form in Google Forms.

1. Go to https://docs.google.com/forms/ and create your own form

2. Add 3 questions to the form, make all questions "short-answer":

![Form](https://github.com/Anas2018EMI/Zillow-Data-Entry-Automation-Bot/blob/f905283d68373de1b91072b9177dce7fdeb141e8/images/2020-08-25_15-20-27-e452a75ff00354982fbac16869f59e1d.png)

3. Click send and copy the link address of the form. You will need to use this in your program.
![Form link](https://github.com/Anas2018EMI/Zillow-Data-Entry-Automation-Bot/blob/2966512c4fb46fb9971093edd378a2e0f5af1cfe/images/2020-08-25_15-21-47-ce68f626cee655ddf83ec94b56eb912f.png)

4. Go to [this web address on Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D) and see how the website is structured, this is where you'll be scraping the data from. Pay attention to the chosen filters. You can choose any location you want. Copy the link of your query in Zillow and paste it in the code:
![Zillow](https://github.com/Anas2018EMI/Zillow-Data-Entry-Automation-Bot/blob/2966512c4fb46fb9971093edd378a2e0f5af1cfe/images/2020-08-25_15-24-26-6abfaeb4f90b56e995d4f0df38b61d05.png)

5. Paste your Zillow search results link and your Google Forms link in the script.

6. Install the corresponding web driver for your Chrome Browser version and paste its path in the code.

7. Paste your user agent of your HTTP header (you can find that in this website).

8. Run the script and enjoy! 😁️
