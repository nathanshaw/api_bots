import os, sys
from sys import platform
import wikipedia
import string
import random
import time
import warnings
import subprocess

number = 1
voices = ["Princess",
          "Fred"]
stop_chars_comma = ["/n", "[", "]", "{", "}", "(", ")", ";", ":"]
stop_chars_space= ['"', "'"]
allowed_chars = [
'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I',
'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2',
'3', '4', '5', '6', '7', '8', '9',',','.', ' '
]

def getRawSummary(term):
    """
    TODO
    """
    raw_summary = None
    try:
        raw_summary = wikipedia.summary(term, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            raw_summary = wikipedia.summary(e.options[random.randrange(0,
                len(e.options))], sentences=1)
        except wikipedia.exceptions.DisambiguationError as e:
            getRawSummary(e.options[random.randrange(0,
                len(e.options))])
        except wikipedia.exceptions.PageError as e:
            pass
    except wikipedia.exceptions.PageError as e:
        pass
    time.sleep(random.randrange(0,10)/5)
    if raw_summary != None:
        return raw_summary
    return seed_term

def processWikiText(raw_summary):
    wiki_summary = ''
    for char in raw_summary:
        if char in allowed_chars:
            wiki_summary += char
        if char in stop_chars_comma:
            wiki_summary += ", "
        if char in stop_chars_space:
            wiki_summary += " "
    wiki_summary = wiki_summary.replace(", .", ".")
    wiki_summary = wiki_summary.replace("  ", " ")
    wiki_summary = wiki_summary.replace(" .", ".")
    wiki_summary = wiki_summary.replace(" ,", ",")
    wiki_summary = wiki_summary.replace(",,", ",")
    wiki_summary = wiki_summary.replace(", ,", ",")
    return wiki_summary

def getSummary(term, voice="Bruce", first_time=False):
    """
    TODO
    """
    search = wikipedia.search(term, 'html.parser')
    raw_summary = getRawSummary(term)
    wiki_summary = processWikiText(raw_summary)

    # time to actually say some things
    if platform == "darwin":
        command = "say -v " + voice + " " + wiki_summary
        print(wiki_summary)
    else:
        if personality == 0:
            if first_time:
                command = 'espeak -s 200 -v f4 "' + wiki_summary + '" \n'
            else:
                command = '"' + wiki_summary + '" \n'
        else:
            if first_time:
                command = 'espeak -s 200 -v m4 "' + wiki_summary + '" \n'
            else:
                command = 'espeak -s 200 -v m4 "' + wiki_summary + '" \n'

        print(wiki_summary)

    try:
        # subprocess.call(command, shell=True)
        print('about to call os.sys')
        time.sleep(random.randrange(6,12)/3)
        os.system(command)
        print('finished call os.sys')
    except Exception as e:
        print("exception thrown : ", e)
        pass

    print(" ")

    last_word = ''.join(
            [c for c in raw_summary.split()[-1] if c.isalpha()])
    return last_word

if len(sys.argv) > 2:
    seed_term = sys.argv[1]
    personality = sys.argv[2]
elif len(sys.argv) > 1:
    seed_term = sys.argv[1]
    print(sys.argv[1])
    personality = voices[random.randrange(len(voices))]
else:
    seed_term = "love"
    personality = voices[random.randrange(len(voices))]

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    while True:
        seed_term = getSummary(seed_term, personality, True)
