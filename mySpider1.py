import requests
from lxml import etree
import re



def looks(url,rule):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    ref_num = selector.xpath(rule[0])
    ref_titl = selector.xpath(rule[1])
    for i in range(40):
        ref_num_c = re.match(b'<span class="threadlist_rep_num center_text" title="&#x56DE;&#x590D;">(.*)</span>&#13;\n',etree.tostring(ref_num[i])).groups()
        ref_titl_c = re.match(b'<a rel="noreferrer" href="(.*)" title="(.*)" target="_blank" class="j_th_tit ">(.*)</a>',etree.tostring(ref_titl[i])).groups()
        a = ref_titl_c[1].decode()
        print ('回复数：',ref_num_c[0].decode())
        print ('标题  ：',a,'\n')                                        



if(__name__ == '__main__'):
    page = 0
    for i in range(5):
        url = 'http://tieba.baidu.com/f?kw=bilibili&ie=utf-8&pn=' + str(page)
        rule = [u'//span[@class = "threadlist_rep_num center_text"]',
                  u'//a[@class="j_th_tit "]']
        looks(url,rule)
        page = page + 50
    








