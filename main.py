import tkinter
import random
from constants import *


class Cell(tkinter.Button):

    def __init__(self, master, x, y, food, wood, rock, *args, **kwargs):
        super(Cell, self).__init__(master, *args, **kwargs)
        self.x=x
        self.y=y
        self.food=food
        self.wood=wood
        self.rock=rock
        print(self.rock)
        self.building = '0'
        self.own='0'


class Playing_Field:

    window = tkinter.Tk()


    def __init__(self):
        #fail=input('Введите название файла шаблона (Без приписки txt)')
        f = open('Template 1.txt')
        #f = open(f'{fail}.txt')
        strings=f.readlines()
        f.close()
        self.squares=[]
        self.ROW=len(strings)
        self.COL=len(strings[1])-1
        for i in range(self.ROW):
            line=[]
            for j in range(self.COL):
                if strings[i][j] == 'F':
                    self.color = 'Olive'
                    self.food = random.randint(1, 3)
                    self.wood = random.randint(2, 6)
                    self.rock = random.randint(0, 2)
                elif strings[i][j] == 'M':
                    self.color = 'Grey'
                    self.food = random.randint(0, 2)
                    self.wood = random.randint(0, 3)
                    self.rock = random.randint(3, 7)
                elif strings[i][j] == 'G':
                    self.color = 'Green'
                    self.food = random.randint(2, 5)
                    self.wood = random.randint(1, 2)
                    self.rock = random.randint(0, 1)
                sqr=Cell(Playing_Field.window, i, j, self.food, self.wood, self.rock, width=4, height=2, bg=COLORS.get(f'{self.color}'))
                line.append(sqr)
            self.squares.append(line)


    def Field_Creation(self):
        for i in range(self.ROW):
            for j in range(self.COL):
                sqr=self.squares[i][j]
                sqr.grid(row=i, column=j)


    def Start(self):
        Playing_Field.window.mainloop()



game=Playing_Field()
game.Field_Creation()
game.Start()
