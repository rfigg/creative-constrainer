import random

print("Creative Constrainer")

instrument = random.choice(['electric guitar','acoustic guitar','piano','keys','beats','bass','drums'])
tempo = random.randint(60,220)
key = random.choice(['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'])+" "+random.choice(['major','minor']) 


print("Play the "+instrument+" in the key of "+key+" at "+str(tempo)+" bpm.")