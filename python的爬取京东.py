import requests
url = "https://item.jd.com/2004139.html"
try:
    r = requests.get(url)
    r.raise_for_status()#r对象的一个方法，就是如果返回的状态吗不为200，就报错
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
