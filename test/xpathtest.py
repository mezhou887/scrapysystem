# -*- coding: utf-8 -*-
'''
Created on 2016年4月7日

@author: 周茂恩
'''
from scrapy.selector import Selector
import unittest

# link1: http://www.cnblogs.com/08shiyan/archive/2013/05/02/3055078.html
# link2: http://www.w3school.com.cn/xpath/index.asp
# link3: http://www.cnblogs.com/ziyunfei/archive/2012/10/05/2710631.html
# link4: http://www.cnblogs.com/think/archive/2006/10/11/525947.html


class TestXpathFunctions(unittest.TestCase):

    sample1 = '''
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

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testSample1(self):
        sel = Selector(text=self.sample1);

        self.assertEqual(sel.xpath('//div/a/@href').extract_first(), 'image1.html')
        self.assertEqual(sel.xpath('//a[re:test(@href, "image\d\S+")]//@src').extract_first(), 'image1_thumb.jpg')        
        self.assertEqual(sel.xpath('//title/text()').extract()[0], 'Example website')
        self.assertEqual(sel.xpath('//base/@href').extract()[0], 'http://example.com/')
        self.assertEqual(sel.xpath('//a[contains(@href, "image2")]/@href').extract()[0], 'image2.html')
        self.assertEqual(sel.xpath('//a[contains(@href, "image2")]/img/@src').extract()[0], 'image2_thumb.jpg')
        self.assertEqual(sel.xpath('//div/a[2]/@href').extract()[0], 'image2.html')
        self.assertEqual(sel.xpath('//div/a[last()]/@href').extract()[0], 'image5.html')
        self.assertEqual(sel.xpath('//a[contains(text(), "image 2")]/@href').extract()[0], 'image2.html')
        
        # 1. [u'image1.html', u'image2.html', u'image3.html', u'image4.html', u'image5.html']
        print '1.', sel.xpath('//div/a/@href').extract()
        
        # 2. [u'image1_thumb.jpg', u'image2_thumb.jpg', u'image3_thumb.jpg', u'image4_thumb.jpg', u'image5_thumb.jpg']
        print '2.', sel.xpath('//a//@src').extract()
        
        # 3. [u'image1.html', u'image2.html']
        print '3.', sel.xpath('//div/a[position()<3]/@href').extract()
        
        # 4. [u'<img src="image1_thumb.jpg">', u'<img src="image2_thumb.jpg">', u'<img src="image3_thumb.jpg">', u'<img src="image4_thumb.jpg">', u'<img src="image5_thumb.jpg">']
        print '4.', sel.xpath('//img[@src]').extract()
        
        # 5. [u'<a href="image1.html">Name: My image 1 <br><img src="image1_thumb.jpg"></a>']
        print '5.', sel.xpath('//div/a[@href="image1.html"]').extract()
        
        # 6. [u'<br>', u'<img src="image2_thumb.jpg">']
        print '6.', sel.xpath('//a[@href="image2.html"]/*').extract()

        # 7. [u'<br>', u'<br>', u'<br>', u'<br>', u'<br>']
        print '7.', sel.xpath('//a/*[1]').extract()  
        
if __name__ == "__main__":
    unittest.main()      
         









