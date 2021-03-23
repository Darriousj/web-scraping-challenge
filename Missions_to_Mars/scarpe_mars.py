#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests 
import os
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


#URL of page being scraped
url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[4]:


#request module
response=requests.get(url)


# In[5]:


soup=bs(response.text,'html.parser')


# In[6]:


#print(soup.prettify())


# In[7]:


news_title=soup.title.text
#news_title


# In[8]:


new_p= soup.body.find_all('p')
#new_p


# In[9]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[10]:


url_img="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(url_img)


# In[11]:


browser.links.find_by_partial_text('FULL IMAGE')[0].click()


# In[12]:


featured_image_url=browser.find_by_css(".fancybox-image")['src']
featured_image_url


# In[13]:


#Mars facts
facts_url='https://space-facts.com/mars/'


# In[14]:


tables = pd.read_html(facts_url)
#tables


# In[15]:


df = tables[0]
df.head()


# In[16]:


html_table = df.to_html()
#html_table


# In[17]:


#html_table.replace('\n', '')


# In[18]:


#df saved to html
df.to_html('table.html')


# In[19]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[20]:


url_hemi="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hemi)


# In[31]:


hempLinks=browser.find_by_css("a.product-item img")
hemis_store=[]
for i in range(len(hempLinks)):
    browser.find_by_css("a.product-item img")[i].click()
    imGurl=browser.links.find_by_text("Sample")["href"]
    tiTle=browser.find_by_css(".title").text
   
    #append the empty array with a dict
    hemis_store.append({"title":tiTle,
                              "img_url":imGurl})
    
    
    browser.back()


# In[32]:


hemis_store


# In[33]:

# Close the browser after scraping 
browser.quit()


# In[ ]:

#Return results
return hemis_store


