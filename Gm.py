from bs4 import BeautifulSoup
import twitter
import numpy as np
from PIL import Image
import os
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
html_doc = '/home/kevinmetro/Desktop/Company-logos/tesla.html'
with open(html_doc) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
lol = soup.get_text()
text = lol.split("\n")
full_text = ""
for x in text:
    full_text = full_text + " " + x


stopwords = set(STOPWORDS)

gm = np.array(Image.open('/home/kevinmetro/Desktop/Company-logos/tslaback.jpg'))
print(gm)
wc = WordCloud(background_color="white", max_words=2000,stopwords=stopwords,mask=gm,width=gm.shape[1],height=gm.shape[0],contour_width=0, contour_color='black')
wc.generate(full_text)
wc.to_file(path.join(d, "tsla.png"))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show() 