import twitter
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

auth_file = "auth.txt"
with open(auth_file) as f:
	auth_list = f.readlines()

consumer_key = auth_list[0].strip('\n')
consumer_secret = auth_list[1].strip('\n')
access_token_key = auth_list[2].strip('\n')
access_token_secret = auth_list[3].strip('\n')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

#print(api.VerifyCredentials())

ncis_results = api.GetSearch(raw_query="q=%23NCIS%20lang%3Aen%20since%3A2016-10-02%20until%3A2016-10-08&src=typd&lang=en")
bbt_results = api.GetSearch(raw_query="q=%23bigbangtheory%20lang%3Aen%20since%3A2016-10-02%20until%3A2016-10-08&src=typd&lang=en")
bull_results = api.GetSearch(raw_query="q=%23bull%20lang%3Aen%20since%3A2016-10-02%20until%3A2016-10-08&src=typd&lang=en")
macgyver_results = api.GetSearch(raw_query="q=%23macgyver%20lang%3Aen%20since%3A2016-10-02%20until%3A2016-10-08&src=typd&lang=en")
madam_results = api.GetSearch(raw_query="q=%23madamsecretary%20lang%3Aen%20since%3A2016-10-02%20until%3A2016-10-08&src=typd&lang=en")
elementary_results = api.GetSearch(raw_query="q=%23elementary%20lang%3Aen%20since%3A2016-10-02%20until%3A2016-10-08&src=typd&lang=en")

results = []
# Major blues scale C, D, D♯/E♭, E, G, A
for twt in ncis_results:
    time = twt.created_at_in_seconds
    tpl = (time, "C")
    results.append(tpl)
for twt in bbt_results:
    time = twt.created_at_in_seconds
    tpl = (time, "D")
    results.append(tpl)
for twt in bull_results:
    time = twt.created_at_in_seconds
    tpl = (time, "D#")
    results.append(tpl)
for twt in macgyver_results:
    time = twt.created_at_in_seconds
    tpl = (time, "E")
    results.append(tpl)
for twt in madam_results:
    time = twt.created_at_in_seconds
    tpl = (time, "G")
    results.append(tpl)
for twt in elementary_results:
    time = twt.created_at_in_seconds
    tpl = (time, "A")
    results.append(tpl)

results.sort(key=lambda tup: tup[0]) 

notes = ""
for i in results:
    notes = notes + i[1] + " "
score = NoteSeq(notes)
midi = Midi(1, tempo=90)
midi.seq_notes(score, track=0)
midi.write("CBStvTwitter.mid")