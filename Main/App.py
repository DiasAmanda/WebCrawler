from Main.Models.Regions import get_states
from Main.Models.Regions import get_cities
from selenium import webdriver
import time

browser = webdriver.Chrome("C:\Users\Amandinha\PycharmProjects\WebCrawler\Drivers\chromedriver.exe")

get_states()
get_cities()

time.sleep(10000)
browser.quit()
