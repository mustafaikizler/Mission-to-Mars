#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)


# In[3]:


#VIsit the mars nasa news website

url = 'https://redplanetscience.com/'
browser.visit(url)

#optional delay
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#Set yup the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


news_article_teaser_body = slide_elem.find('div',  class_='article_teaser_body').get_text()
news_article_teaser_body


# ### Featured Images
# 

# In[8]:


url = 'https://spaceimages-mars.com/#'
browser.visit(url)

#find and click the full image button


# In[9]:


full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


#find the relative image URL

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


img_url = f'https://spaceimages-mars.com/#{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com/#')[0]

df.columns=['description','Mars', 'Earth']

df.set_index('description', inplace = True)

df


# In[14]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[20]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)




# In[59]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range(4):
    

    hemispheres = {}


    browser.find_by_tag('img.thumb')[i].click()
    html = browser.html
    title_soup = soup(html, 'html.parser')
    title = title_soup.find("h2", class_="title").text
    image = title_soup.find("a", string="Sample")["href"]


    image_url= url + image
    browser.back()
    
    
    hemispheres["image_url"] = image_url
    
    hemispheres["title"] = title
    
    
    hemisphere_image_urls.append(hemispheres)


    
    


# In[60]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


# # 5. Quit the browser
# browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




