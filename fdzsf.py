class Caracter:
    def __init__(self,pers):
        print(',.')

    def run(self):
        print('бежит')    

    def shoot(self):
        print('стреляет')

    def take(self):
       print('берет предмет')

       
class Human(Caracter):
    def __init__(self,pers):
        print('появился человек')
        
    def life(self,caracter):
        
        
class Warlok(Caracter):
    def __init__(self,pers):
        print('появился маг')
    def fly(self):
        print('letit')
    
 
       
        
class Hunter(Human):
    def __init__(self,pers):
        print('появился человек')

class HunterFly(Warlok):
    def __init__(self,pers):
        print('появился человек2')
        
pers=Caracter('A')
human_pers = Hunter(Human(Caracter))
human_pers.life(pers)

pers=Caracter('B')
warlok_pers = HunterFly(Human(Caracter))
warlok_pers.life(pers)
