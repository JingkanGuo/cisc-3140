import urllib.request
import json
import webbrowser


apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=VL5mDHDfWjXWVqMjVovoy8T2Xmdx3I4IZg4TCQbc'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

data = json.loads(apodread.decode('utf-8'))

print("\n\nCoverted python data")
print(data)

#input('\nPress Enter to open NASA Picture of the Day in Chrome')
#webbrowser.open(decodeapod['url'])

GEN_HTML = "index.html"

f = open(GEN_HTML, 'w')

message = """
<html>
<center>
<head>
</title><h1>Astronomy Picture of the Day</h1></title>
</head>
<body>
<p>%s</p>
<img src = "%s" />
<p>%s</p>
<p>copyright:%s</p>
<p>Explanation:%s</p>
</body>
</center>
"""%(data["date"],data["url"],data["title"],data["copyright"],data["explanation"])

f.write(message)

f.close()

webbrowser.open(GEN_HTML, new = 1)