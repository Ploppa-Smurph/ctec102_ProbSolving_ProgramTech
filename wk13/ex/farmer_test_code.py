# this is a test program for you, after you wrote your farmer class run this code:
from farmer_class1 import Farmer
#initializing 2 class instances: 
brian=Farmer('Brian', 2)
lenny=Farmer ('Lenny', 3)
print('farmers info before: ')
print(brian)
print(lenny)
#farmer 1 talks to farmer 2:
brian.talk_to(lenny)
print('farmer info after: ')
print(brian)

''' Results when runnning the program:
===== RESTART: C:/Users/vladi/Dropbox/BPCC/    
farmers info before: 
This is Brian. His mood index is 2
This is Lenny. His mood index is 3
Brian : I rather like  Lenny
Brian : my mood improved!
farmer info after: 
This is Brian. His mood index is 3'''
