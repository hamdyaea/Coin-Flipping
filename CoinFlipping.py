#!/usr/bin/env python3
#
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import random
from easygui import *
import sys


class Coin:
    def __init__(self):
        self.Coin.easyHead
        self.Coin.easyTail
        self.Coin.fullIMG


Coin.easyHead = "./images/face.gif"
Coin.easyTail = "./images/pile.gif"
Coin.fullIMG = "./images/full.gif"


def head():
    inputNum = 2
    outputNum = list(range(inputNum + 1))
    outputNum.remove(0)
    random.shuffle(outputNum)
    top2 = outputNum[:1]

    if top2 == [1]:

        coinChoice = ["Replay", "Quit"]
        message = "You Win !\n\n\nThe result is head"
        msgCenter = message.center(100)
        replay = buttonbox(
            image=Coin.easyHead,
            choices=coinChoice,
            title="Coin Flipping",
            msg=msgCenter,
        )
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)

    else:
        coinChoice = ["Replay", "Quit"]
        message = "You lose !\n\n\nThe result is tail"
        msgCenter = message.center(100)
        replay = buttonbox(
            image=Coin.easyTail,
            choices=coinChoice,
            title="Coin Flipping",
            msg=msgCenter,
        )
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
        message = "You Win !\n\n\nThe result is tail"
        msgCenter = message.center(100)
        replay = buttonbox(
            image=Coin.easyTail,
            choices=coinChoice,
            title="Coin Flipping",
            msg=msgCenter,
        )
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)

    else:
        coinChoice = ["Replay", "Quit"]
        message = "You lose !\n\n\nThe result is head"
        msgCenter = message.center(100)
        replay = buttonbox(
            image=Coin.easyHead,
            choices=coinChoice,
            title="Coin Flipping",
            msg=msgCenter,
        )
        if replay == "Replay":
            begin()
        else:
            sys.exit(0)


def begin():
    yourChoice = ["Tail", "Head"]
    message = "Please select tail or head"
    msgCenter = message.center(80)
    play = buttonbox(
        image=Coin.fullIMG, choices=yourChoice, title="Coin Flipping", msg=msgCenter
    )
    if play == "Tail":
        tail()
    elif play == "Head":
        head()
    else:
        sys.exit(0)


begin()
