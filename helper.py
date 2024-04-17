import requests

from lxml import html
from random import choice, randint


def is_valid(word):
    url = f"http://wordnetweb.princeton.edu/perl/webwn?s={word.lower().replace('q', 'qu')}"
    request = requests.get(url)
    return bool(html.fromstring(request.content).xpath("//div[@class='key']"))


def letter_gen():
    DICE = [
        "RIFOBX",
        "IFEHEY",
        "DENOWS",
        "UTOKND",
        "HMSRAO",
        "LUPETS",
        "ACITOA",
        "YLGKUE",
        "QBMJOA",
        "EHISPN",
        "VETIGN",
        "BALIYT",
        "EZAVND",
        "RALESC",
        "UWILRG",
        "PACEMD",
    ]
    while DICE:
        die = DICE.pop(randint(0, len(DICE) - 1))
        yield choice(die)
    # Testing:
    # x = [
    #     ["A", "X", "G", "A"],
    #     ["S", "A", "N", "T"],
    #     ["Q", "I", "E", "D"],
    #     ["E", "L", "O", "T"],
    # ]
    # yield from x


A = """ ___                                 .--.           
(   )                               (_  |          
 | |.-.     .--.     .--.     .--.    | |    .--.   
 | /   \   /    \   /    \   /    \   | |   /    \  
 |  .-. | |  .-. ; ;  ,-. ' ;  ,-. '  | |  |  .-. ; """

B = """ | |  | | | |  | | | |  | | | |  | |  | |  |  | | | 
 | |  | | | |  | | | |  | | | |  | |  | |  |  |/  | 
 | |  | | | |  | | | |  | | | |  | |  | |  |  ' _.' """

C = """ | '  | | | '  | | | '  | | | '  | |  | |  |  .'.-. 
 ' `-' ;  '  `-' / '  `-' | '  `-' |  | |  '  `-' / 
  `.__.    `.__.'   `.__. |  `.__. | (___)  `.__.'  
                    ( `-' ;  ( `-' ;                
                     `.__.    `.__.                 """
