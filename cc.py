import random
import sys

print("Creative Constrainer")

# pick random creative constraints
instrument = random.choice(['electric guitar','acoustic guitar','piano','keys','beats','bass','drums'])
tempo = random.randint(60,220)
key = random.choice(['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'])+" "+random.choice(['major','minor']) 

# start of sentence to build with cmd line options
message = 'Play '

# build sentence with all options if none are specified
if len(sys.argv)==1 or '--instrument' in sys.argv or '-i' in sys.argv:
	message += 'the '+instrument+' '
if len(sys.argv)==1 or '--key' in sys.argv or '-k' in sys.argv:
	message += 'in the key of '+key+' '
if len(sys.argv)==1 or '--tempo' in sys.argv or '-t' in sys.argv:
	message += 'at '+str(tempo)+' bpm.'

# check for case of single invalid argument
if message != 'Play ':
	print(message)
else:
	print("Play the "+instrument+" in the key of "+key+" at "+str(tempo)+" bpm.")