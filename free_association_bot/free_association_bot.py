import os, sys
import wikipedia
import string
import random
import time

"""
Female
------
Agnes - Robotic
Kathy -
Princess - sounds small but good
Vicki -
Victoria -

Male
------
Bruce
Fred
Junior
Ralph

Novelty
-------
Albert
"Bad News"
Bahh
Bells
Boing
Bubbles
Cellos
Deranged
"Good News"
Hysterical
"Pipe Organ"
Trinoids
Whisper
Zarvox
"""
stop_punc = ["[", "]", "(", ")", "{", "}", "'", '"', ";", "-"]
# TODO instead of replacing the punctuation instead give a comma

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
    # time.sleep(random.randrange(0,10)/5)
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

    print(wiki_summary)
    os.system("say -v " + voice + " " + wiki_summary)
    print("-------------- " + voice + " ------------------------------")

    last_word = ''.join(
            [c for c in raw_summary.split()[-1] if c.isalpha()])

    if last_word != term and len(last_word) > 0:
        getSummary(last_word, voice)
    else:
        getSummary(seed_term, voice)


seed_term = sys.argv[1]
if len(sys.argv) > 2:
    personality = sys.argv[2]
else:
    print(sys.argv[1])
    personality = "Princess"

getSummary(seed_term, personality)
