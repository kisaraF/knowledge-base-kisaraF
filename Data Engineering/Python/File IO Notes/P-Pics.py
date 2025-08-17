import requests
from bs4 import BeautifulSoup
import os

res= requests.get('https://www.pornpics.com/galleries/modern-day-sins-featuring-river-lynn-tommy-pistol-hot-porn-pics-74033670/')
# res= requests.get('https://www.pornpics.com/galleries/lustful-blondie-in-sexy-lingerie-kiara-lord-having-a-masturbation-session-70031968/')
#print(res.status_code)

soup= BeautifulSoup(res.content, 'html.parser')

imgs= soup.select('.rel-link')
print(len(imgs))

img_links=[]

for i in range(0,len(imgs)):
    #img_links.append(imgs[i].get('href',None))
    name= f"Photo {i+1}"
    link= imgs[i].get('href',None)
    
    with open(name + '.jpg', 'wb') as f:
        im= requests.get(link)
        f.write(im.content)
    print(link)
    print(f"{name} created")
    
    

