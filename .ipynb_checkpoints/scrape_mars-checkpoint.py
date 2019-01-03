{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# imports\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Site Navigation\n",
    "executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars NASA News\n",
    "news_url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(news_url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Five Things to Know About InSight's Mars Landing\n",
      "NASA engineers will be holding their breath when their spacecraft heads into Mars' atmosphere on Nov. 26.\n"
     ]
    }
   ],
   "source": [
    "article = soup.find(\"div\", class_='list_text')\n",
    "news_title = article.find(\"div\", class_=\"content_title\").text\n",
    "news_p = article.find(\"div\", class_ =\"article_teaser_body\").text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#JPL Mars Space Images\n",
    "image_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(image_url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA22801-640x350.jpg\n"
     ]
    }
   ],
   "source": [
    "image = soup.find(\"img\", class_=\"thumb\")[\"src\"]\n",
    "featured_image_url = \"https://www.jpl.nasa.gov\" + image\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather\n",
    "tweet_url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(tweet_url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sol 2213 (2018-10-27), high -12C/10F, low -70C/-93F, pressure at 8.74 hPa, daylight 06:11-18:29\n"
     ]
    }
   ],
   "source": [
    "mars_weather = soup.find(\"p\", class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text\n",
    "print(mars_weather) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Facts\n",
    "facts_url = \"https://space-facts.com/mars/\"\n",
    "browser.visit(facts_url)\n",
    "mars_data = pd.read_html(facts_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars hemispheres\n",
    "hemisphers_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemisphers_url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_hemisphere = []\n",
    "\n",
    "products = soup.find(\"div\", class_ = \"result-list\" )\n",
    "hemispheres = products.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "for hemisphere in hemispheres:\n",
    "    title = hemisphere.find(\"h3\").text\n",
    "    title = title.replace(\"Enhanced\", \"\")\n",
    "    end_link = hemisphere.find(\"a\")[\"href\"]\n",
    "    image_link = \"https://astrogeology.usgs.gov/\" + end_link    \n",
    "    browser.visit(image_link)\n",
    "    html = browser.html\n",
    "    soup=BeautifulSoup(html, \"html.parser\")\n",
    "    downloads = soup.find(\"div\", class_=\"downloads\")\n",
    "    image_url = downloads.find(\"a\")[\"href\"]\n",
    "    mars_hemisphere.append({\"title\": title, \"img_url\": image_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
