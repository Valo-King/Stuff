noun = []
verbIng = []
pastVerb = []

for i in range(13):
    nouns = input("Enter a noun: ")
    noun.append(nouns.lower())
for i in range(3):
    verb = input("Give me a verb ending in 'ing.': ") 
    verbIng.append(verb.lower())
for i in range(5):
    verb = input("Give me a verb in the past tense.: ")
    pastVerb.append(verb.lower())
exclamation = input("What do you exclaim when you're suprised?: ")
adj = input("Describe something in one word.: ")
adjColour = input("What's your favorite colour?: ")
adverb = input("Give me an adverb.: ")
plu = input("What about a plural noun?: ")
place = input("I also need a place, if you'd believe me.: ")
print("“Put your hands up” said the " + noun[0] + ". “You’re under arrest for " + verbIng[0] + " the " + noun[1] + " at the " + noun[2] +  "“." + exclamation.upper() + "“ though Frank. His hands were " + verbIng[1] + " like " + plu + " on a " + noun[3] + ". This wasn’t the first time he had " + pastVerb[0] + " a " + noun[4] + " and he knew he was in " + adj + " trouble. Just moments before Frank " + pastVerb[1] + " into a " + noun[5] + " and " + pastVerb[2] + " a " + noun[6] + " and a " + noun[7]  + ". He was spotted and a big " + noun[8] + " chased after him and " + pastVerb[3] + " him in the " + noun[9] + ". Now Frank was surrounded and had no choice but to surrender. So it was off to " + place + " for Frank. Frank was the " + adjColour + " sheep in his " + noun[10] + " , always " + verbIng[2] + " into trouble. It started when Frank " + pastVerb[4] + " a " + noun[11] + " from his neighbor and " + adverb + " rode the " + noun[12] + " home.")