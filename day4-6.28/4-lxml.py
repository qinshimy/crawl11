from lxml import etree

tree = etree.parse('./data.html')

ret = tree.xpath('//title/text()')

print(ret)

ret = tree.xpath('//li[@class="haha"]/text()')
print(ret)

ret = tree.xpath('//li[contains(@class,"h")]/text()')

print(ret)

ret = tree.xpath('//li[last()]/text()')
print(ret)

ret = tree.xpath('//div[@id="pp"]/ol[last()]/li/@*')
print(ret)

ret = tree.xpath('//li[not(contains(@class,"h"))]/text()')

print(ret)

ret = tree.xpath('//li[@id="hehe"][@class="nene"]/text()|//li[@class="lala"]/text()')

print(ret)