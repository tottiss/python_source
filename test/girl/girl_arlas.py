__author__ = 'Administrator'
import re,time,os,requests,random

def get_response(url):
    headers = {
        "headers" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"
    }

    response = requests.get(url, headers = headers)
    return response

def get_page_urls():
    url = 'http://girl-atlas.com'
    page_urls=[]
    page_urls.append(url)
    response = get_response(url)

    while(True):
        parsed_body=response.text
        result = re.findall(r'class="btn-form next"\shref="(\S+)"', parsed_body)
        if not len(result):
            break
        nexturl=url+result[0]

        page_urls.append(nexturl)
        response=get_response(nexturl)
    return page_urls

def get_album_url(url):
    album_urls=[]

    for x in url:
        response=get_response(x)
        parsed_body=response.text
        result = re.findall(r"http://girl-atlas.com/a/\d+", parsed_body)
        if not len(result):
            break
        album_urls.append(result[0])
    return album_urls

def get_image_url(url):
    images_urls=[]
    arr=[]

    for x in url:
        response=get_response(x)
        parsed_body=response.text
        result = re.findall("http://girlatlas.b0.upaiyun.com.*?jpg", parsed_body)
        if not len(result):
            break
        for img in result:
            images_urls.append(img)

        match = re.search(r'href="http://girl-atlas.com/t/\d+">(.*?)</a></li>', parsed_body)
        try:
            title = match.group(1)
        except:
            print x+"error"

        girl_dict={title:images_urls}
        arr.append(girl_dict)
    return arr

def download(girl_list):
    dirpath='E:/girl'
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    for girl in girl_list:
        urls=girl.values()[0]
        dirname=dirpath+"/"+girl.keys()[0]
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        for x in urls:
            match = re.search(r"\w+.jpg", x)
            if match:
                filename = match.group()

            file=dirname+"/"+str(filename)
            print x

            with open(file,'wb') as f:
                response=get_response(x)
                if(response):
                    f.write(response.content)

if __name__ == '__main__':

    start_time = time.time()
    #page_urls = get_page_urls()

    page_urls=['http://girl-atlas.com']

    album_urls=get_album_url(page_urls)
    image_urls=get_image_url(album_urls)
    download(image_urls)

    elapsed_time = time.time() - start_time
    print "elasped %s seconds!!!!" % elapsed_time