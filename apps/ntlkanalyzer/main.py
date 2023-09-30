from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = [
    "VADER is smart, handsome, and funny.",
    "VADER is smart, handsome, and funny!",
    "VADER is very smart, handsome, and funny.",
    "VADER is VERY SMART, handsome, and FUNNY.",
    "VADER is VERY SMART, handsome, and FUNNY!!!",
    "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",
    "The book was good.",
    "The book was kind of good.",
    "The plot was good, but the characters are uncompelling and the dialog is not great.",
    "A really bad, horrible book.",
    "At least it isn't a horrible book.",
    ":) and :D",
    "",
    "Today sux",
    "Today sux!",
    "Today SUX!",
    "Today kinda sux! But I'll get by, lol",
    "VW-Aktie nachbörslich etwas tiefer: Netzwerkstörung legt Volkswagen lahm - Produktionsstillstand auch bei Audi - Störungsdauer ungewiss",
    "VW share slightly lower in after-hours trading: Network fault paralyzes Volkswagen - Production standstill also at Audi - Duration of fault uncertain",
]

for sentence in sentences:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
