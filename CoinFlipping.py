# Developer : Hamdy Abou El Anein

import random
from easygui import *
import sys





easyHead = "./images/face.gif"
easyTail = "./images/pile.gif"
fullIMG = "./images/full.gif"

def head():
    inputNum = 2
    outputNum = list(range(inputNum + 1))
    outputNum.remove(0)
    random.shuffle(outputNum)
    top2 = outputNum[:1]

    if top2 == [1]:

        coinChoice = ["Replay", "Quit"]

        replay = buttonbox(image=easyHead, choices=coinChoice, title="Coin Flipping",
                           msg="You Win !\n\nThe result is head")
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)


    else:
        coinChoice = ["Replay", "Quit"]
        replay = buttonbox(image=easyTail, choices=coinChoice, title="Coin Flipping",
                           msg="You loose !\n\nThe result is tail")
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)


def tail():
    inputNum = 2
    outputNum = list(range(inputNum + 1))
    outputNum.remove(0)
    random.shuffle(outputNum)
    top2 = outputNum[:1]


    if top2 == [1]:

        coinChoice = ["Replay", "Quit"]

        replay = buttonbox(image=easyTail, choices=coinChoice, title="Coin Flipping",
                           msg="You Win !\n\nThe result is tail")
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)


    else:
        coinChoice = ["Replay", "Quit"]
        replay = buttonbox(image=easyHead, choices=coinChoice, title="Coin Flipping",
                           msg="You loose !\n\nThe result is head")
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)


def begin():
    yourChoice = ["Tail","Head"]
    play = buttonbox(image=fullIMG, choices=yourChoice, title="Coin Flipping",
                       msg="Please select tail or head")
    if play == "Tail":
        tail()
    elif play == "Head":
        head()
    else:
        sys.exit(0)

begin()