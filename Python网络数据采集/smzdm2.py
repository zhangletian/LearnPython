import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# headers=("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

url = 'http://www.smzdm.com/jingxuan/p9/'
req = urllib.request.Request(url, headers=headers)
html = urlopen(req)

bsObj = BeautifulSoup(html)

nameList = []

nameSet = bsObj.findAll('span',{'class':'feed-hot-title'})

for name in nameSet:
	nameList.append(name.string)

print(nameList)

                                                                            #<div class="feed-hot-card">
                                                                                        #<a target="_blank" href="http://www.smzdm.com/p/7564672" onclick="dataLayer.push({'event':'23200','tab':'全部','position':'10','pagetitle':'促销活动 : 天猫聚划算 必胜客  披萨意面加甜点'})">
                                                #<div class="feed-hot-pic"><img src="//tp-qny.smzdm.com/201707/22/5972b433a93b25933.png_d200.jpg" alt=""  width="154px" height="154px" style="margin-top:0px" ></div>
                                                #<div class="feed-hot-title">促销活动 : 天猫聚划算 必胜客  披萨意面加甜点</div>
                                                #<span class="z-highlight">爆款好价，惊喜有礼，麻辣小龙虾比萨低至49元</span>
                                            #</a>
                                        #</div>
                                                                            #<div class="feed-hot-card">
                                                                                        #<a target="_blank" href="http://www.smzdm.com/p/7558614" onclick="dataLayer.push({'event':'23200','tab':'全部','position':'11','pagetitle':'Serta 舒达 Sertapedic® 系列 Madagan Euro-top 床垫 Queen'})">
                                                #<div class="feed-hot-pic"><img src="//tp-y.zdmimg.com/201705/23/5923fdf533ab39225.jpg_d200.jpg" alt=""  width="154px" height="154px" style="margin-top:0px" ></div>
                                                #<div class="feed-hot-title">Serta 舒达 Sertapedic® 系列 Madagan Euro-top 床垫 Queen</div>
                                                #<span class="z-highlight">5999元包邮（需用券）</span>
                                            #</a>
                                        #</div>
                                                                            #<div class="feed-hot-card">
                                                                                        #<a target="_blank" href="http://www.smzdm.com/p/7564688" onclick="dataLayer.push({'event':'23200','tab':'全部','position':'12','pagetitle':'历史低价 : ARROW 箭牌卫浴 AB1116 喷射虹吸式马桶'})">
                                                #<div class="feed-hot-pic"><img src="//tp-qny.smzdm.com/201707/22/5972b65e1831f4372.jpg_d200.jpg" alt=""  width="154px" height="154px" style="margin-top:0px" ></div>
                                                #<div class="feed-hot-title">历史低价 : ARROW 箭牌卫浴 AB1116 喷射虹吸式马桶</div>
                                                #<span class="z-highlight">699元包邮（双重优惠）</span>
                                            #</a>
                                        #</div>
