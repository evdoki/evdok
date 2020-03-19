# -*- coding: utf-8 -*-
class Game:    
    def __init__(self, new_name='User',x=0,y=0):        
        self._name = new_name # новое имя
        print(f'New player {self._name}')
        self._level = 0
        self._speedsubject = 0
        self._airsubject = 10
        self._intelligencesubject = 0
        self.x = x
        self.y = y
        self._life = 5
        # level player
    
    def fly(self):
        print(f"Игрок {self._name}")
        if self._level < 25: # если уровень
            print(f"Игрок {self._name} не умеет летать")
        else:
            print(f"Игрок {self._name} умеет летать")
            
            
    def __add__(self, other):
        return Game(self.x + other.x, self.y + other.y)
    
    
    def gaming(self):
        if self._speedsubject > 0:
            self.x += 5
            print(f'{self._name} ускорился')
        elif self._speedsubject < 0:
            self.x -= 5
            print(f'{self._name} замедлился')

            
    def air(self):
        if 0 < self.x < 10 and 0 < self.y < 100:
            self._airsubject += 1 # счетчик кислорода
        else:
            self._airsubject -= 1
            print(f'{self._name} испытывает кислородное голодание {self._aircsubject}')
        if self._airsubject == 0:
            print(f'{self._name} умер')
            self._level = 0
            self._speedsubject = 0
            self._airsubject = 10
            self._intelligencesubject = 0
            self.x = 0
            self.y = 0            
            self._life -= 1
            if self._life == 0:
                print('Game over')
                #тут должен игрок удалиться я хз как делать, в инете не очень понятно
        
    def intelligence(self):
        if self._life > 0 and self._airsubject > 20:
            self._intelligencesubject += 1
        if self._intelligencesubject %10 == 0:
            self._level += 1
        
      
my_player1 = Game()
my_player1.set_name("Вася")

my_player1.gaming()
my_player2 = Game('Ксюша')
