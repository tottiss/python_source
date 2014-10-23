import string, urllib2
for i in range(1,30000,1):
    url='http://www.jz.cc/gongsi-'+str(i)+".html"

    sName="html/"+str(i)+'.html'
    f=open(sName,"w+")
    read=urllib2.urlopen(url).read()
    f.write(read)
    f.close()