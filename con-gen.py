#!/usr/bin/python3

import random

def main():
    who = {
        1 : "The government",
        2 : "Bill Gates and his cohort",
        3 : "Immigrants",
        4 : "The Gays",
        5 : "Doctors",
        6 : "People",
        7 : "The Japanese",
        8 : "Corporations",
        9 : "Atheists",
        10 : "NASA",
        11 : "Liberals",
        12 : "Facebook",
        13 : "Lizard people",
        14 : "Morning News Networks",
        15 : "The Jews",
        16 : "The Clintons"
    }

    what = {
        1 : "the TV",
        2 : "abortions",
        3 : "nanotechnology",
        4 : "Satan",
        5 : "video games",
        6 : "feminism",
        7 : "pesticides",
        8 : "the sun's rays",
        9 : "dihydrogen monoxyide",
        10 : "lies and propaganda",
        11 : "GMOs",
        12 : "vaccinations",
        13 : "holographic simulations",
        14 : "deep drilling",
        15 : "high-fructose corn syrup",
        16 : "realistic clones"
    }

    why = {
        1 : "cause cancer",
        2 : "give children autism",
        3 : "erode your brain",
        4 : "turn people gay",
        5 : "make you fat",
        6 : "amass enormous wealth",
        7 : "cause global warming",
        8 : "destroy America",
        9 : "turn you into a sheep",
        10 : "kill bees at an alarming rate",
        11 : "take over the world",
        12 : "hide the aliens",
        13 : "communicate with dolphins",
        14 : "bring back Michael Jackson"
    }
    
    who_num = random.randint(1,len(who))
    what_num = random.randint(1,len(what))
    why_num = random.randint(1,len(why))

    if (who[who_num].endswith("s")):
        print("{} are using {} to {}!".format(who[who_num], what[what_num],
                                             why[why_num]))
    elif (who[who_num].endswith("e")):
        print("{} are using {} to {}!".format(who[who_num], what[what_num],
                                             why[why_num]))
    elif (who[who_num][:4] == "Bill"):
        print("{} are using {} to {}!".format(who[who_num], what[what_num],
                                             why[why_num]))
    else:
        print("{} is using {} to {}!".format(who[who_num], what[what_num],
                                             why[why_num]))


if __name__ == "__main__":
    main();
