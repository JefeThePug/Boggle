import requests

from random import choice, randint


def is_valid(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower().replace('q', 'qu')}"
    request = requests.get(url)
    return isinstance(request.json(), list)


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


A = r""" ___                                 .--.           
(   )                               (_  |          
 | |.-.     .--.     .--.     .--.    | |    .--.   
 | /   \   /    \   /    \   /    \   | |   /    \  
 |  .-. | |  .-. ; ;  ,-. ' ;  ,-. '  | |  |  .-. ; """

B = r""" | |  | | | |  | | | |  | | | |  | |  | |  |  | | | 
 | |  | | | |  | | | |  | | | |  | |  | |  |  |/  | 
 | |  | | | |  | | | |  | | | |  | |  | |  |  ' _.' """

C = r""" | '  | | | '  | | | '  | | | '  | |  | |  |  .'.-. 
 ' `-' ;  '  `-' / '  `-' | '  `-' |  | |  '  `-' / 
  `.__.    `.__.'   `.__. |  `.__. | (___)  `.__.'  
                    ( `-' ;  ( `-' ;                
                     `.__.    `.__.                 """
