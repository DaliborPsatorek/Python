from people import *
from random import randint  

def ALFABET():
    ALFABET = ""
    for x in range(91):
        if(x<65):
            continue
        ALFABET += f'\"{chr(x)}\",'
    return ALFABET

def alfabet():
    alfabet = ""
    for x in range(123):
        if(x<97):
            continue
        alfabet += f'\"{chr(x)}\",'
    return alfabet

class personClass():
    def __init__(self,name = 'test ',surname = 'test', age = 0,sex = 'test'):
        self.name= name
        self.surname= surname
        self.age= age
        self.sex= sex
        
def randomPerson(): 
    x = randint(0,201)
    y = randint(0,201)
    if(x > 100 or y > 100):
        sex = "Female"
    else:
        sex = "Male"
    return personClass(names[x],surnames[y],randint(1,100),sex)

def printPerson(object):
    print(f'{chr(123)} name: "{object.name}" surname: "{object.surname}" age: "{object.age}" sex: "{object.sex}" {chr(125)}')

freands = []
for x in range(5):
    freands.append(randomPerson())

for x in range(5):
    printPerson(freands[x])

