import tkinter
import random
from constants import *


class Cell(tkinter.Button):

    def __init__(self, master, x, y, food, wood, rock, terrain, own, cell_cost, *args, **kwargs):
        super(Cell, self).__init__(master, *args, **kwargs)
        self.x=x
        self.y=y
        self.food=food
        self.wood=wood
        self.rock=rock
        self.terrain=terrain
        self.cell_cost=cell_cost
        self.building = 'Пусто'
        self.own=own

    def Change_Owner(self, Color):
        self.own=Color


class Playing_Field:

    window = tkinter.Tk()
    window.geometry("505x500")


    def __init__(self):
        #fail=input('Введите название файла шаблона (Без приписки txt)')
        f = open('Template 1.txt')
        #f = open(f'{fail}.txt')
        strings=f.readlines()
        f.close()
        self.res_yellow={'food':4,'wood':4, 'rock':0, 'money':6}
        self.res_blue={'food':4,'wood':4, 'rock':0, 'money':6}
        self.squares=[]
        self.ROW=len(strings)
        self.COL=len(strings[1])-1
        for i in range(self.ROW):
            line=[]
            for j in range(self.COL):
                self.own = 'Black'
                difference=i-j
                if difference<0:
                    difference = difference * -1
                self.cell_cost = (self.COL-1)-difference
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

                sqr=Cell(Playing_Field.window, i, j, self.food, self.wood, self.rock, self.terrain, self.own, self.cell_cost, width=4, height=2, bg=COLORS.get(f'{self.color}'))
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
        self.building=pressed_square.building
        self.cell_cost=pressed_square.cell_cost
        self.l1.config(text=f"Координаты клетки x={self.x}, y={self.y}\nПлодородность клетки = {self.food}\n"
                            f"Лесистость клетки = {self.wood}\nГористость клетки = {self.rock}\n"
                            f"Местность = {self.terrain}\nПостройка = {self.building}\nХозяин = {self.own}")
        self.l2.config(text=f"Стоимость клетки={self.cell_cost}")
        self.l4.config(
            text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Камень = {self.res_player.get('rock')}"
                 f", Монеты = {self.res_player.get('money')}")


    def Field_Creation(self):
        for i in range(self.ROW):
            for j in range(self.COL):
                sqr=self.squares[i][j]
                sqr.grid(row=i, column=j)
        self.l1=tkinter.Label(text="Координаты клетки x=-, y=-\nПлодородность клетки = -\n"
                            "Лесистость клетки = -\nГористость клетки = -\n"
                            "Местность = -\nПостройка = -\nХозяин = -", bg=COLORS.get('Silver'), justify=tkinter.LEFT)
        self.l2=tkinter.Label(text="Стоимость клетки=-", bg=COLORS.get('Olive'))
        self.l4=tkinter.Label(text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Камень = {self.res_player.get('rock')}"
                                   f", Монеты = {self.res_player.get('money')}", bg=COLORS.get('Grey'))


        self.b1=tkinter.Button(text='Купить', command=game.Buying_cell, bg=COLORS.get('Olive'))
        self.b1.place(x=460, y=111)



        self.l1.place(x=342, y=1)
        self.l2.place(x=342, y=112)
        self.l4.place(x=0, y=369)


    def Update(self):
        self.l1.config(text=f"Координаты клетки x={self.x}, y={self.y}\nПлодородность клетки = {self.food}\n"
                            f"Лесистость клетки = {self.wood}\nГористость клетки = {self.rock}\n"
                            f"Местность = {self.terrain}\nПостройка = {self.building}\nХозяин = {self.own}")
        self.l4.config(text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Камень = {self.res_player.get('rock')}"
                                   f", Монеты = {self.res_player.get('money')}")


    def Buying_cell(self):
        if self.res_player.get('money')>=self.cell_cost and self.own=='Black':
            self.res_player['money']=self.res_player.get('money') - self.cell_cost
            self.squares[self.x][self.y].Change_Owner(Player_color)
        game.Update()



    def Start(self):
        if Player_color=="Yellow":
            self.res_player=self.res_yellow
        else:
            self.res_player = self.res_blue
        game.Field_Creation()
        Playing_Field.window.mainloop()


Player_color='Yellow'
game = Playing_Field()
game.Start()
