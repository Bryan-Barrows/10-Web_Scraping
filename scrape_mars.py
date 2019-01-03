# imports
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

#Site Navigation
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# Defining scrape
def scrape():
	mars_data = {}
	mars_data["mars_news"] = marsTitle()
	mars_data["mars_paragraph"] = marsNews()
	mars_data["mars_image"] = marsImage()
	mars_data["mars_weather"] = marsWeather()
	mars_data["mars_facts"] = marsFacts()
	mars_data["mars_hemisphere"] = marsHem()

	return mars_data

# Mars NASA News

def marsTitle():
	news_url = "https://mars.nasa.gov/news/"
	browser.visit(news_url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")

	article = soup.find("div", class_='list_text')
	news_title = article.find("div", class_="content_title").text
	return news_title

def marsNews():
	news_url = "https://mars.nasa.gov/news/"
	browser.visit(news_url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")

	article = soup.find("div", class_='list_text')
	news_p = article.find("div", class_ ="article_teaser_body").text
	return news_p

#JPL Mars Space Images

def marsImage():
	image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(image_url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")

	image = soup.find("img", class_="thumb")["src"]
	featured_image_url = "https://www.jpl.nasa.gov" + image
	return featured_image_url

# Mars Weather

def marsWeather():
	tweet_url = "https://twitter.com/marswxreport?lang=en"
	browser.visit(tweet_url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")

	mars_weather = soup.find("p", class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
	return mars_weather

# Mars Facts

def marsFacts():
	facts_url = "https://space-facts.com/mars/"
	browser.visit(facts_url)
	mars_data = pd.read_html(facts_url)
	mars_data = pd.DataFrame(mars_data[0])
	mars_table = mars_data.to_html(header = False, index = False)
	mars_facts = mars_table.replace('\n','')
	return mars_facts

# Mars Hemispheres

def marsHem(): 
	hemisphers_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(hemisphers_url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")

	mars_hemisphere = []

	products = soup.find("div", class_ = "result-list" )
	hemispheres = products.find_all("div", class_="item")

	for hemisphere in hemispheres:
	    title = hemisphere.find("h3").text
	    title = title.replace("Enhanced", "")
	    end_link = hemisphere.find("a")["href"]
	    image_link = "https://astrogeology.usgs.gov/" + end_link    
	    browser.visit(image_link)
	    html = browser.html
	    soup=BeautifulSoup(html, "html.parser")
	    downloads = soup.find("div", class_="downloads")
	    image_url = downloads.find("a")["href"]
	    dictionary = {"title": title, "img_url": image_url}
	    mars_hemisphere.append(dictionary)

	return mars_hemisphere
