#!/usr/bin/python3

import random

def main():
    who = [
        "The government",
        "Bill Gates and his cohort",
        "Immigrants",
        "The Gays",
        "Doctors",
        "People",
        "The Japanese",
        "Corporations",
        "Atheists",
        "NASA",
        "Liberals",
        "Facebook",
        "Lizard people",
        "Morning news networks",
        "The Jews",
        "The Clintons"
    ]

    what = [
        "the TV",
        "abortions",
        "nanotechnology",
        "Satan",
        "video games",
        "feminism",
        "pesticides",
        "the sun's rays",
        "dihydrogen monoxyide",
        "lies and propaganda",
        "GMOs",
        "vaccinations",
        "holographic simulations",
        "deep drilling",
        "high-fructose corn syrup",
        "realistic clones"
    ]

    why = [
        "cause cancer",
        "give children autism",
        "erode your brain",
        "turn people gay",
        "make you fat",
        "amass enormous wealth",
        "cause global warming",
        "destroy America",
        "turn you into a sheep",
        "kill bees at an alarming rate",
        "take over the world",
        "hide the aliens",
        "communicate with dolphins",
        "bring back Michael Jackson"
    ]
    
    who_num = random.randint(0,(len(who) - 1))
    what_num = random.randint(0,(len(what)- 1))
    why_num = random.randint(0,(len(why) - 1))

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
