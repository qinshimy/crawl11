
from lxml import etree





str = '''<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div></body></html>
'''
tree = etree.HTML(str)
# result = etree.tostring(tree)
# print(result.decode('utf-8'))

ret = tree.xpath('//li')

ret = tree.xpath('./body/div/ul/li')

ret = tree.xpath('//li/@class')

ret = tree.xpath('//li/a[@href="link1.html"]')

ret = tree.xpath('//ul')[0]
print(ret)
li = ret.xpath('./li')

print(li)

print(ret.xpath('//div'))


print('-------------------------',ret.xpath('./ul'))








print(ret)
