from lxml import etree

books = '''
<?xml version="1.0" encoding="utf-8"?>
<bookstore> 
  <book category="cooking"> 
    <title lang="en">Everyday Italian</title>  
    <author>Giada De Laurentiis</author>  
    <year>2006</year>  
    <price>30.00</price> 
  </book>  
  <book category="children"> 
    <title lang="en">Harry Potter</title>  
    <author>J K. Rowling</author>  
    <year>2006</year>  
    <price>29.99</price> 
  </book>  
  <book category="web"> 
    <title lang="en">XQuery Kick Start</title>  
    <author>James McGovern</author>  
    <author>Per Bothner</author>  
    <author>Kurt Cagle</author>  
    <author>James Linn</author>  
    <author>Vaidyanathan Nagarajan</author>  
    <year>2003</year>  
    <price>49.99</price> 
  </book> 
  <book category="web" cover="paperback"> 
    <title lang="en">Learning XML</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>39.95</price> 
  </book> 
</bookstore>
'''

tree = etree.HTML(books)

ret = tree.xpath('//book[price>30]/title/text()')
print(ret)


ret = tree.xpath('//book[year mod 2=1 and price>30]/author/text()')
print(ret)