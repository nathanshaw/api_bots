import os, sys
from sys import platform
import wikipedia
import string
import random
import time
import subprocess

number = 1
voices = ["Princess",
          "Fred"]
stop_punc = ["[", "]", "{", "}", "'", '"', "-"]
comma_stop = ["(",  ")", ";", ":"]


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
    time.sleep(random.randrange(0,7)/5)
    if raw_summary != None:
        return raw_summary
    return seed_term

def getSummary(term, voice="Bruce"):
    """
    TODO
    """
    search = wikipedia.search(term, 'html.parser')
    raw_summary = getRawSummary(term)

    wiki_summary = ''.join([c for c in raw_summary if c not in stop_punc])
    wiki_summary = ''
    for c in raw_summary:
        if c not in stop_punc and c not in comma_stop:
            wiki_summary += c
        elif c in comma_stop:
            wiki_summary += ","
        else:
            wiki_summary += " "

    if platform == "darwin":
        command = "say -v " + voice + " " + wiki_summary
        print('voice : ',  voice, ': "', wiki_summary, '"')
    else:
        command = 'say ' + wiki_summary
	print(wiki_summary)
    try:
        subprocess.call(command, shell=True)
    except UnicodeEncodeError:
        print("passing...")

    print("")

    try:
        last_word = ''.join(
            [c for c in raw_summary.split()[-1] if c.isalpha()])
    except:
        last_word = seed_term    

    if last_word != term and len(last_word) > 0:
        getSummary(last_word, voice)
    else:
        getSummary(seed_term, voice)


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

getSummary(seed_term, personality)
