'''
frameworks for scraping with python

Beautiful soup - this is a parsing library for simple tasks, neededs another library to fetch te html/xml file before navigating and searching the parse tree
scrapy - powerful framework for webcrawling and webscraping, desighned for largescale scaling aand crawling projects
    - can be used with scrapy for more compelex tasks
    - can handle http requests
selenium - powerful l;ibrary maily for web automation and testing but can also be used for building scrapers
    - allows for broser automation across multiple browsers, i.e you can simulate user interations with web pages
    - it is opensource and supports a vast number of programming languages 
    - can be used foe webscraping too especially when dealng with websites that rely heavily on javascript
COMPNENTS OF SELENIUM
w Selenium WebDriver - provides an API to automate the browser and simulate user actions
selenium IDE - a broswer extension that helps record and playback user interactions making it easier to create test scripts
selenium Grid - helps run tests on multiple browsers and machines simultaneously
'''

from selenium import webdriver
from selenium.webdriver.common.by import By #for locating elements on the web page

#since i am using the latest verion of selenium, I do not need to explicitly download webdrivers although I can still choose to


# now let's initialize a webdriver assume we are using firefox
fox_driver = webdriver.Firefox()
 # next we can navigate to a web page

fox_driver.get("https://books.toscrape.com/")

# read the title of the page
title = fox_driver.title
print("Page title is:", title, f"and the url of the page is {fox_driver.current_url}")

book_list = fox_driver.find_elements(By.CLASS_NAME, "col-xs-6 col-sm-4 col-md-3 col-lg-3") 
#book1 = fox_driver.find_element(By.TAG_NAME,"h3").find_element(By.CSS_SELECTOR, "[title='A Light in the Attic']")
for book in book_list:
    rating = book.find_element(By.TAG_NAME, "p").get_attribute("class")
    title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    price = book.find_element(By.CLASS_NAME, "price_color").text
    availability = book.find_element(By.CLASS_NAME, "instock availability").text
    print(f"Title: {title}, Price: {price}, Rating: {rating}, Availability: {availability}")

fox_driver.quit()