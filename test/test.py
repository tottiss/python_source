import webbrowser as web
import urllib

url="http://meiriyiwen.com/"
content=urllib.urlopen(url).read()
open("a.html","w").write(content)
web.open_new_tab("a.html")
