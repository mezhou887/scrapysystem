from scrapy.selector import Selector

html = '''
<html>
    <head>
        <base href='http://example.com/' />
        <title>Example website</title>
    </head>
    <body>
        <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
            <a href='imageA.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
        </div>
    </body>
</html>
'''

sel = Selector(text=html);
print '1.', sel.xpath('//title/text()').extract(); # [u'Example website']
print '2.', sel.xpath('//base/@href').extract(); # [u'http://example.com/']
print '3.', sel.xpath('//div/a/@href').extract(); # [u'image1.html', u'image2.html', u'image3.html', u'image4.html', u'image5.html']
print '4.', sel.xpath('//div/a/@href').extract_first(); # image1.html
print '5.', sel.xpath('//a[contains(@href, "image2")]/@href').extract(); # [u'image2.html']
print '6.', sel.xpath('//a[contains(@href, "image2")]/img/@src').extract(); # [u'image2_thumb.jpg']
print '7.', sel.xpath('//a//@src').extract(); # [u'image1_thumb.jpg', u'image2_thumb.jpg', u'image3_thumb.jpg', u'image4_thumb.jpg', u'image5_thumb.jpg']
print '8.', sel.xpath('//a[re:test(@href, "image\d\S+")]//@src').extract_first(); # image1_thumb.jpg
