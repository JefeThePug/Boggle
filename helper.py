import requests
from lxml import html

def is_valid(word):
    url = f"http://wordnetweb.princeton.edu/perl/webwn?s={word}"
    request = requests.get(url)
    return bool(html.fromstring(request.content).xpath("//div[@class='key']"))
