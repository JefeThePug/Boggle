import requests

from lxml import html
from random import choice, randint

def is_valid(word):
    url = f"http://wordnetweb.princeton.edu/perl/webwn?s={word}"
    request = requests.get(url)
    return bool(html.fromstring(request.content).xpath("//div[@class='key']"))

def letter_gen():
    DICE = [
        "RIFOBX", "IFEHEY", "DENOWS", "UTOKND",
        "HMSRAO", "LUPETS", "ACITOA", "YLGKUE",
        "QBMJOA", "EHISPN", "VETIGN", "BALIYT",
        "EZAVND", "RALESC", "UWILRG", "PACEMD",
    ]
    while DICE:
        die = DICE.pop(randint(0, len(DICE) - 1))
        yield choice(die)
