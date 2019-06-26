from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
url_1= "https://www.amazon.in/Apple-iPhone-Xs-64GB-Space/dp/B07JVC6QRY/ref=sr_1_1?keywords=Apple+iPhone+XS+64+GB+Space+Grey&qid=1561478114&s=gateway&sr=8-1"
url_2= "https://www.flipkart.com/apple-iphone-xs-max-space-grey-64-gb/p/itmf944egfh8mgvg?pid=MOBF944EEFJDUYH6&srno=s_1_1&otracker=search&otracker1=search&lid=LSTMOBF944EEFJDUYH6EOFYSJ&fm=SEARCH&iid=26f4db10-d32e-4667-94b9-e2e1529cef76.MOBF944EEFJDUYH6.SEARCH&ppt=sp&ppn=sp&ssid=uc65un2yr40000001561478085783&qH=6b2069d42aa67f90"
url_3= "https://paytmmall.com/apple-iphone-xs-64-gb-space-grey-CMPLXMOBAPPLE-IPHONEDUMM141E11C015F-pdp?product_id=210076984&channel=WEB&discoverability=online&src=grid&svc=-1&tracker=%7C%7C%7C%7C%2Fg%2Fmobiles-tablets%2Fiphone-xs-llpid-183177%7C183177%7C1%7C%7C%7C%7C&get_review_id=210074899"

uClient_1 = urlopen(url_1)
page_html = uClient_1.read()
uClient_1.close()
page_soup_1 = soup(page_html,"html.parser")
uClient_2 =urlopen(url_2)
page_html = uClient_2.read()
uClient_2.close()
page_soup_2 = soup(page_html,"html.parser")
uClient_3 =urlopen(url_3)
page_html = uClient_3.read()
uClient_3.close()
page_soup_3 = soup(page_html,"html.parser")

website_1="AMAZON"
website_2="FLIPKART"
website_3="PAYTM"

name_1= page_soup_1.findAll("span",{"id":"productTitle"})[0].text.strip()
price_1=page_soup_1.findAll("span",{"id":"priceblock_ourprice"})[0].text.strip()[2:]
price_1=price_1[:price_1.find(".")]
price_1=price_1.replace(",","")
rating_1 =page_soup_1.findAll("i",{"class":"a-star-4-5"})[0].text.strip()
rating_1=rating_1[:rating_1.find(" ")]


name_2= page_soup_2.findAll("span",{"class":"_35KyD6"})[0].text.strip()
price_2=page_soup_2.findAll("div",{"class":"_1vC4OE"})[0].text.strip()[1:]
price_2=price_2.replace(",","")
rating_2 =page_soup_2.findAll("div",{"class":"hGSR34"})[0].text.strip()


name_3= page_soup_3.findAll("h1",{"class":"NZJI"})[0].text.strip()
price_3=page_soup_3.findAll("span",{"class":"_1V3w"})[0].text.strip()
rating_3 =page_soup_2.findAll("div",{"class":"hGSR34"})[0].text.strip()
price_3=price_3.replace(",","")


dataframe_list = [
    [website_1,name_1,int(price_1),rating_1],
    [website_2,name_2,int(price_2),rating_2],
    [website_3,name_3,int(price_3),rating_3]
]
df = pd.DataFrame(np.array(dataframe_list),[0,1,2],['Sites','name','price','rating'])
print("Comparison Table")
print(df)
print("Bar Graph")
plt.interactive(False)
df.rating=pd.to_numeric(df.rating)
df.price=pd.to_numeric(df.price)
df.plot.bar()
plt.show()

