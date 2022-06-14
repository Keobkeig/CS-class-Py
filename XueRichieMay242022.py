#!/usr/bin/python
print("Content-Type: text/html\n\n")

import random

nouns =["Payment", "Farmer", "Kick", "Fall", "Taste", "Horses", "Worm", "Degree", "Skirt", "Accident", "Berry", "Fight", "Heart", "Experience", "Front", "Birds", "Significance", "Door", "Hat", "Leadership" ]
verbs =["Step", "Sow", "Bid", "Think", "Shake", "Scare", "Weave", "Yawn", "Distribute", "Leap", "Ingest", "Constrain", "Corrod", "Sack", "Come", "Fly", "Express", "Free", "Prosecute", "Part", "Remake", "Sail", "Obstruct", "Address", "Multiply", "Guide", "Weigh", "Induce", "Constitute", "Melt"]
adjectives =["Whispering", "Condemned", "Wistful", "Oafish", "Tall", "New", "Resolute", "Auspicious", "Jaded", "Defeated", "Free", "Early", "Bashful", "Handsomely", "Feigned", "Premium", "Wholesale", "Hilarious", "Royal", "Pumped", "Eight", "Various", "Peaceful", "Naive", "Wacky"]
adverbs = ["obediently","possibly","completely","repeatedly","thoroughly","fully","mortally","rapidly","blindly","famously","faithfully","forth","promptly","quietly","tediously","zestfully","well","automatically","steadily","therefore"]
places = ["Great Barrington", "Hackensack", "Stamford", "Bridgeton", "Lansing" ,"Tiffin" ,"Woods Hole" ,"Bartlesville" ,"Massena" ,"Ridgewood"]

text3 =  "{NAME1} {VERB}. {PLACE1} {NAME1} {VERB}. {NAME2} {VERB}. {NAME2} {VERB}. {NAME3} {NAME3} {NAME3} !"
names = ["Mario", "Link", "Ash" ,"Samus", "Bowser", "Ganon", "Motherbrain", "Jessie", "James", "Meowth", "Pikachu","Charmander","Squirtle","Bulbasaur"]

text4 = "The first {PLACE1} is straightforward. There are no obstacles, you just need to {VERB} them together! {VERB} {ADJECTIVE} will help your {NOUN}. {NAME1} will move based on your proximity, so {VERB} them into one group, then {VERB} {ADVERB} them all and force them {ADJECTIVE}! For the second {PLACE2} , a conniving {NAME2} is {VERB} back and forth across the field. If your {NAME1} get too {ADJECTIVE} , they'll {VERB} in the opposite direction. You can actually use this to your {NOUN}. Push the {NAME1} forward before the {NAME2} starts moving back to the {NOUN}. This will scare all the {NAME2} to the {NOUN}, making it {ADJECTIVE} to push them against the {NOUN} and into the goal. But wait! There's a {NOUN} blocking entry to the goal! Gym Trainer {NAME3} has his {ADJECTIVE} {NAME5} , but nothing else! Now onto the fourth section. Now there are four dividers with {NOUN} that are more {ADJECTIVE}. And two {NAME6} . You can never be {ADJECTIVE} with more {NAME6} . Let's employ a similar tactic. Wait for the {NAME6} on the right to turn the corner and {VERB} against the wall. This is the time to {VERB} all the {NAME1} against the right wall, then push them along the wall until you hit the goal."
 
def replaceNamesAndPlaces(text,namesList,placesList):
    for i in range(1,10):
        replaceName = "{NAME" + str(i) + "}"
        replacePlace = "{PLACE" + str(i) + "}"
        randomName = random.choice(namesList)
        randomPlace = random.choice(placesList)
        if replaceName in text:
            while randomName in text:
                randomName = random.choice(namesList)
            text = text.replace(replaceName, randomName)
        if replacePlace in text:
            while randomPlace in text:
                randomPlace = random.choice(placesList)
            text = text.replace(replacePlace, randomPlace)     
    return text


def replaceWords(text,nounList,verbList,adjectiveList, adverbList):
    while text.find("{NOUN}") > -1:
        text = text[:text.find("{NOUN}")] + random.choice(nounList) + text[text.find("{NOUN}") + 6:]
    while text.find("{ADJECTIVE}") > -1:
        text = text[:text.find("{ADJECTIVE}")] + random.choice(adjectiveList) + text[text.find("{ADJECTIVE}") + 11:]
    while text.find("{VERB}") > -1:
        text = text[:text.find("{VERB}")] + random.choice(verbList) + text[text.find("{VERB}") + 6:]
    while text.find("{ADVERB}") > -1:
        text = text[:text.find("{ADVERB}")] + random.choice(adverbList) + text[text.find("{ADVERB}") + 8:]
    return text

print(replaceWords(replaceNamesAndPlaces(text4,names,places), nouns, verbs, adjectives, adverbs))
print(replaceWords(replaceNamesAndPlaces(text3,names,places), nouns, verbs, adjectives, adverbs))

#sample output: Pikachu {VERB}. Pikachu {VERB}. Jessie {VERB}. Jessie {VERB}. Bowser Bowser Bowser!