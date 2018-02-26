import requests
from lxml import etree



def looks(url,rule):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath(rule)
    for i in range(9):
        print(etree.tostring(content_field[i]))



if(__name__ == '__main__'):
    url = 'http://tieba.baidu.com/f?kw=bilibili&fr=index&red_tag=k0670506289'
    rule = u'//span[@class = "threadlist_rep_num center_text"]'
    looks(url,rule)
    
