# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import thread
import time
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

print u'正在加载中请稍候......'

f=open("a.txt","w+")
page=1
while(page>0):
    myUrl = "http://m.qiushibaike.com/hot/page/"+str(page)

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(myUrl, headers = headers)
    myResponse=urllib2.urlopen(req)
    myPage = myResponse.read()
    unicodePage = myPage.decode("utf-8")

    myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',myPage,re.S)

    if myItems:
        print u'第%d页' % page
        f.write("----------第"+str(page)+"页----------\n")
        page+=1
        for item in myItems:
            strs=item[0].replace("\n","")+"\t"+item[1].replace("\n","")+"\n"
            f.write(strs)
    else:
        break;
f.close()