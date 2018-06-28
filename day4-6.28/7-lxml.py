import urllib
import urllib.request

from lxml import etree

import os
url = 'http://sc.chinaz.com/tupian/fengjing.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')

tree = etree.HTML(html)

pic = tree.xpath('//div[@class="box picblock col3"]/div/a/img/@src2')
picname = tree.xpath('//div[@class="box picblock col3"]/div/a/img/@alt')
picD = tree.xpath('//div[@class="box picblock col3"]/div/a/@href')

# for i in range(len(pic)):
#     suffix = os.path.splitext(pic[i])[-1]
#     urllib.request.urlretrieve(url=pic[i],filename='./pic/%s%s'%(picname[i],suffix))

for i in range(len(pic)):
    request = urllib.request.Request(url=picD[i], headers=headers)
    response = urllib.request.urlopen(request)

    html = response.read().decode('utf-8')

    tree = etree.HTML(html)
    Pic = tree.xpath('//div[@class="dian"]/a/@href')
    Pic = Pic[0]


    suffix = os.path.splitext(Pic)[-1]
    urllib.request.urlretrieve(url=Pic,filename='./pcc/%s%s'%(picname[i],suffix))

'''http://pic2.sc.chinaz.com/Files/pic/pic9/201806/bpic7271_s.jpg'''