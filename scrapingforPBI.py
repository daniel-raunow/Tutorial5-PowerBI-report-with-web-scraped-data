from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
country_codes = ["FI", "SE", "NO", "DK", "IS"]
no_of_bands = []
population = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for code in country_codes:
    url_to_get = "https://www.metal-archives.com/lists/" + code
    driver.get(url_to_get)
    time.sleep(3)
    table_object = driver.find_element("xpath", 
                                      "//div[contains(@class, 'dataTables_info')]")
    web_text = table_object.get_attribute("innerHTML")
    bands = int(web_text.split()[5].replace(",",""))
    no_of_bands.append(bands)
    
for country in countries:
    url_to_get = "https://en.m.wikipedia.org/wiki/Demographics_of_" + country
    driver.get(url_to_get)
    time.sleep(3)
    table_object_wiki = driver.find_element("xpath",
                                            "//td[contains(@class, 'infobox-data')]")
    web_text = table_object_wiki.get_attribute("innerHTML")
    if country == 'Sweden':
        pop_no = int(web_text.split()[15].replace(",",""))
    else:
        pop_no = int(web_text.split()[0].replace(",",""))
    population.append(pop_no)


table_for_report = pd.DataFrame()
table_for_report["country"] = countries
table_for_report["No_of_bands"] = no_of_bands
table_for_report["Population"] = population
print(table_for_report)
