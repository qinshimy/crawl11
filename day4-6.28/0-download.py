
import urllib
import urllib.request
import urllib.parse

import re
url = 'https://music.163.com/discover/toplist?id=19723756'

url_real = 'http://music.163.com/song/media/outer/url?id=%s.mp3'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

def get_musicid():

    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = '<a href="/song\?id=([\d]+)">(.*?)</a>'
    p = re.compile(pattern)
    musics = p.findall(content)
    return musics


def get_music(music):
    for i in music:
        url2 = url_real%(i[0])
        urllib.request.urlretrieve(url=url2,filename='./music/%s.mp3'%(i[1]))
        print('歌曲：%s下载成功 ！' % (i[1]))


if __name__ == '__main__':

    music = get_musicid()

    get_music(music)