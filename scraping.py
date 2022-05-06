
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)

#VIsit the mars nasa news website

url = 'https://redplanetscience.com/'
browser.visit(url)

#optional delay
browser.is_element_present_by_css('div.list_text', wait_time=1)

#Set yup the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

news_article_teaser_body = slide_elem.find('div',  class_='article_teaser_body').get_text()
news_article_teaser_body

# ### Featured Images

url = 'https://spaceimages-mars.com/#'
browser.visit(url)

#find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

html = browser.html
img_soup = soup(html, 'html.parser')


#find the relative image URL

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


img_url = f'https://spaceimages-mars.com/#{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com/#')[0]

df.columns=['description','Mars', 'Earth']

df.set_index('description', inplace = True)

df

df.to_html()

browser.quit()

