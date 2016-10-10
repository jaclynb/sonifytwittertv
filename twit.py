"""
Usage: 
twit.py FILE TAG1 TAG2 TAG3 TAG4 TAG5 TAG6
twit.py -h

Give 6 hashtags without the hash symbol to search for in Twitter 
and be sonified, in order, to the major blues scale

Options:
    -h, --help

"""

import twitter
from docopt import docopt
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

def main(arguments):
    # Authenticate on Twitter
    auth_file = "auth.txt"
    with open(auth_file) as f:
    	auth_list = f.readlines()
    f.close()

    consumer_key = auth_list[0].strip('\n')
    consumer_secret = auth_list[1].strip('\n')
    access_token_key = auth_list[2].strip('\n')
    access_token_secret = auth_list[3].strip('\n')

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    # Clean up arguments so it's just a list of hashtags
    arguments.pop('--help', None) #Remove --help option
    filename = arguments.pop('FILE', None) + ".mid"

    # Search for each of the given hashtags individually
    comboResults = []
    for key in sorted(set(arguments)):
        comboResults.append(api.GetSearch(term="%23" + arguments[key]))

    # Create list of times and notes 
    # Each hashtag has its own note
    # Major blues scale C, D, D♯/E♭, E, G, A
    scale = ["C", "D", "D#", "E", "G", "A"]
    results = []
    for i in range(len(comboResults)):
        for twt in comboResults[i]:
            results.append((twt.created_at_in_seconds, scale[i]))

    # Sort notes in place by time
    results.sort(key=lambda tup: tup[0]) 

    # Get a list of just notes
    notes = ""
    for i in results:
        notes = notes + i[1] + " "

    # Create MIDI file
    score = NoteSeq(notes)
    midi = Midi(1, tempo=90)
    midi.seq_notes(score, track=0)
    midi.write(filename)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)