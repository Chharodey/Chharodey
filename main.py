import tkinter
import random
from constants import *


#Класс отвечающий за каждую отдельную кнопку на игровом поле
class Cell(tkinter.Button):

    def __init__(self, master, x, y, food, wood, rock, terrain, own, *args, **kwargs):
        super(Cell, self).__init__(master, *args, **kwargs)
        self.x=x
        self.y=y
        self.food=food
        self.wood=wood
        self.rock=rock
        self.terrain=terrain
        print(self.rock)
        self.building = '0'
        self.own=own


class Playing_Field:

    window = tkinter.Tk()
    window.geometry("505x500")


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
                self.own = 'Black'
                if strings[i][j] == 'F':
                    self.color = 'Olive'
                    self.food = random.randint(1, 3)
                    self.wood = random.randint(2, 6)
                    self.rock = random.randint(0, 2)
                    self.terrain = 'Forest'
                elif strings[i][j] == 'M':
                    self.color = 'Grey'
                    self.food = random.randint(0, 2)
                    self.wood = random.randint(0, 3)
                    self.rock = random.randint(3, 7)
                    self.terrain = 'Mountains'
                elif strings[i][j] == 'G':
                    self.color = 'Green'
                    self.food = random.randint(2, 5)
                    self.wood = random.randint(1, 2)
                    self.rock = random.randint(0, 1)
                    self.terrain = 'Grass'
                elif (strings[i][j] == 'Y') or (strings[i][j] == 'B'):
                    self.color = 'Silver'
                    self.food = 0
                    self.wood = 0
                    self.rock = 0
                    self.terrain = 'Сastle'
                    if strings[i][j] == 'Y':
                        self.own = 'Yellow'
                    else:
                        self.own = 'Blue'

                sqr=Cell(Playing_Field.window, i, j, self.food, self.wood, self.rock, self.terrain, self.own, width=4, height=2, bg=COLORS.get(f'{self.color}'))
                sqr.config(command=lambda button = sqr: self.clicking_on_square(button))
                line.append(sqr)
            self.squares.append(line)


    def clicking_on_square(self, pressed_square):
        self.food = pressed_square.food
        self.wood = pressed_square.wood
        self.rock = pressed_square.rock
        self.x = pressed_square.x
        self.y = pressed_square.y
        self.own = pressed_square.own
        self.terrain=pressed_square.terrain
        self.l1.config(text=f"Координаты клетки x={self.x}, y={self.y}\nПлодородность клетки = {self.food}\n"
                            f"Лесистость клетки = {self.wood}\nГористость клетки = {self.rock}\n"
                            f"Местность = {self.terrain}\nХозяин = {self.own}")


    def Field_Creation(self):
        for i in range(self.ROW):
            for j in range(self.COL):
                sqr=self.squares[i][j]
                sqr.grid(row=i, column=j)
        self.l1=tkinter.Label(text=f"Координаты клетки x=-, y=-\nПлодородность клетки = -\n"
                            f"Лесистость клетки = -\nГористость клетки = -\n"
                            f"Местность = -\nХозяин = -", bg=COLORS.get('Silver'), justify=tkinter.LEFT)
        self.l1.place(x=342, y=1)


    def Start(self):
        Playing_Field.window.mainloop()



game=Playing_Field()
game.Field_Creation()
game.Start()
