#!/usr/bin/python3

import random

def main():
    who = [
        ("The government", False),
        ("Bill Gates and his cohort", True),
        ("Immigrants", True),
        ("The Gays", True),
        ("Doctors", True),
        ("Bill Bellichek and the Illuminati", True),
        ("The Japanese", True),
        ("Corporations", True),
        ("Atheists", True),
        ("NASA", False),
        ("Liberals", True),
        ("Facebook", False),
        ("Lizard people", True),
        ("Morning news networks", True),
        ("The Jews", True),
        ("The Clintons", True)
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
        "realistic clones",
        "bitcoin"
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
        "bring back Michael Jackson",
        "abolish the patriarchy"
    ]
    
    who_num = random.randint(0,(len(who) - 1))
    what_num = random.randint(0,(len(what)- 1))
    why_num = random.randint(0,(len(why) - 1))

    if (who[who_num][1]):
        print("{} are using {} to {}!".format(who[who_num][0], what[what_num],
                                             why[why_num]))
    else:
        print("{} is using {} to {}!".format(who[who_num][0], what[what_num],
                                             why[why_num]))


if __name__ == "__main__":
    main();
