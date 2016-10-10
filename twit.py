import twitter
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

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

ncis_results = api.GetSearch(term="%23NCIS")
bbt_results = api.GetSearch(term="%23bigbangtheory")
bull_results = api.GetSearch(term="%23bull")
macgyver_results = api.GetSearch(term="%23macgyver")
madam_results = api.GetSearch(term="%23madamsecretary")
elementary_results = api.GetSearch(term="%23elementary")

# Major blues scale C, D, D♯/E♭, E, G, A
results = []
for twt in ncis_results:
    results.append((twt.created_at_in_seconds, "C"))
for twt in bbt_results:
    results.append((twt.created_at_in_seconds, "D"))
for twt in bull_results:
    results.append((twt.created_at_in_seconds, "D#"))
for twt in macgyver_results:
    results.append((twt.created_at_in_seconds, "E"))
for twt in madam_results:
    results.append((twt.created_at_in_seconds, "G"))
for twt in elementary_results:
    results.append((twt.created_at_in_seconds, "A"))

results.sort(key=lambda tup: tup[0]) 

notes = ""
for i in results:
    notes = notes + i[1] + " "

score = NoteSeq(notes)
midi = Midi(1, tempo=90)
midi.seq_notes(score, track=0)
midi.write("CBStvTwitter.mid")