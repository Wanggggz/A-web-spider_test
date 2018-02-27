import requests
from lxml import etree
import re


def looks(url,rule):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    ref_num = selector.xpath(rule[0])
                                                
    
    
    for i in range(0,49):
        ref_num_c = re.match(b'<span class="threadlist_rep_num center_text" title="&#x56DE;&#x590D;">(.*)</span>&#13;\n',etree.tostring(ref_num[i])).groups()

        print ('回复数：',ref_num_c[0].decode())
                                                



if(__name__ == '__main__'):
    page = 0
    for i in range(2):
        url = 'http://tieba.baidu.com/f?kw=bilibili&ie=utf-8&pn=' + str(page)
        rule = [u'//span[@class = "threadlist_rep_num center_text"]',
                  u'//span[@class = "tb_icon_author"]']
        looks(url,rule)
        page = page + 50
    
