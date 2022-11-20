import random
import sys

print("Creative Constrainer")

# pick random creative constraints
instrument = random.choice(['electric guitar','acoustic guitar','piano','keys','beats','bass','drums'])
tempo = random.randint(60,220)
key = random.choice(['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'])+" "+random.choice(['major','minor']) 
signature = random.choice(['2/4','3/4','4/4','5/4','11/4','2/2','6/8','9/8','12/8','7/8'])

# start of sentence to build with cmd line options
message = 'Play'

# build sentence with all options if none are specified
if len(sys.argv)==1 or '--instrument' in sys.argv or '-i' in sys.argv:
	message += ' the '+instrument
if len(sys.argv)==1 or '--key' in sys.argv or '-k' in sys.argv:
	message += ' in the key of '+key
if len(sys.argv)==1 or '--tempo' in sys.argv or '-t' in sys.argv:
	message += ' at '+str(tempo)+' bpm'
if len(sys.argv)==1 or '--signature' in sys.argv or '-s' in sys.argv:
	message += ' in '+signature+' time'
message += '.'

# check for case of single invalid argument
if message != 'Play':
	print(message)
else:
	print("Play the "+instrument+" in the key of "+key+" at "+str(tempo)+" bpm in "+signature+" time.")