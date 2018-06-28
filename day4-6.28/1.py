#!user/bin/env python3
# -*- coding: gbk -*-
import urllib
import urllib.request

import urllib.parse
import re
# url = 'https://music.163.com/#/search/m/?s=%s&type=1'
#
# url_real = 'http://music.163.com/song/media/outer/url?id=%s.mp3'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

# key = input('请输入歌名或者歌手：')
# key = urllib.parse.quote(key).encode('utf-8')
# url1 = url % (key)
# request = urllib.request.Request(url=url1,headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# pattern = r'<a href="/song?id=([\d]+)">'
# p = re.compile(pattern)
# musicids = p.findall(content)
# print(musicids)

import re
content = '''<li><a href="/song?id=571338279">往后余生（翻自 马良）</a></li><li><a href="/song?id=862099538">第五人格</a></li><li><a href="/song?id=574922126">Connection</a></li><li><a href="/song?id=573125026">Waiting For</a></li>'''
# <a href="/song?id=487593280">   a id="song_487593939"
pattern = r'<a href="/song\?id=([\d]+)">(.*?)</a>'
p = re.compile(pattern)
musicids = p.findall(content)
print(musicids)

#
# url = 'https://music.163.com/search/m/?s=%E5%BC%A0%E6%9D%B0&type=1'
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# with open('./2.html','w',encoding='utf-8') as fp:
#     fp.write(content)