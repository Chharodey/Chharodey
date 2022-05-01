import tkinter
from random import *
from constants import *


class Cell(tkinter.Button):

    def __init__(self, master, x, y, food, wood, clay, rock, ore, gold, gem, terrain, own, cell_cost, *args, **kwargs):
        super(Cell, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.food = food
        self.wood = wood
        self.clay = clay
        self.rock = rock
        self.ore = ore
        self.gold = gold
        self.gem = gem
        self.terrain = terrain
        self.cell_cost = cell_cost
        self.building = 'Пусто'
        self.own = own

    def Change_Owner(self, Color):
        self.own=Color

    def Change_Building(self, building):
        self.building=building


class Playing_Field:

    window = tkinter.Tk()
    window.geometry("505x500")


    def __init__(self):
        #fail=input('Введите название файла шаблона (Без приписки txt)')
        f = open('Template 1.txt')
        #f = open(f'{fail}.txt')
        strings=f.readlines()
        f.close()
        self.cell_cost = 'x'
        self.name = 'x'
        self.res_yellow={'food':4,'wood':4, 'rock':0, 'money':6}
        self.res_blue={'food':4,'wood':4, 'rock':0, 'money':6}
        self.normal_price={'food':1,'wood':randint(2,3)}
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
                    self.food = randint(1, 3)
                    self.wood = randint(2, 6)
                    self.clay = 0
                    self.rock = randint(0, 2)
                    self.ore = 0
                    self.gold = 0
                    self.gem=0
                    self.terrain = 'Лес'
                elif strings[i][j] == 'M':
                    self.color = 'Grey'
                    self.food = randint(0, 2)
                    self.wood = randint(0, 3)
                    self.clay = 0
                    self.rock = randint(3, 7)
                    self.ore = randint(1, 4)
                    a = randint(1, 10)
                    if a < 5:
                        self.gold = randint(1,2)
                    elif a == 5:
                        self.gold = 3
                    else:
                        self.gold = 0
                    a=randint(1, 10)
                    if a==1:
                        self.gem = 1
                    else:
                        self.gem = 0
                    self.terrain = 'Горы'
                elif strings[i][j] == 'G':
                    self.color = 'Green'
                    self.food = randint(2, 5)
                    self.clay = randint(0, 1)
                    self.wood = randint(1, 2)
                    self.rock = randint(0, 1)
                    self.ore = 0
                    self.gold = 0
                    self.gem = 0
                    self.terrain = 'Луг'
                elif strings[i][j] == 'H':
                    self.color = 'Brown'
                    self.food = randint(2, 4)
                    self.clay = randint(2, 4)
                    self.wood = randint(1, 2)
                    self.rock = randint(0, 1)
                    self.ore = 0
                    self.gold = 0
                    self.gem = 0
                    self.terrain = 'Холм'
                elif strings[i][j] == 'R':
                    self.color = 'Aqua'
                    self.food = 0
                    self.clay = randint(3, 8)
                    self.wood = 0
                    self.rock = 0
                    self.ore = 0
                    a = randint(1, 100)
                    if a < 21:
                        self.gold = 1
                    else:
                        self.gold = 0
                    a = randint(1, 100)
                    if a < 6:
                        self.gem = 2
                    elif a < 26:
                        self.gem = 1
                    else:
                        self.gem = 0
                    self.terrain = 'Река'
                elif (strings[i][j] == 'Y') or (strings[i][j] == 'B'):
                    self.color = 'Silver'
                    self.food = 0
                    self.wood = 0
                    self.clay = 0
                    self.rock = 0
                    self.ore = 0
                    self.gold = 0
                    self.gem = 0
                    self.terrain = 'Замок'
                    if strings[i][j] == 'Y':
                        self.own = 'Yellow'
                    else:
                        self.own = 'Blue'

                sqr=Cell(Playing_Field.window, i, j, self.food, self.wood, self.clay, self.rock, self.ore, self.gold, self.gem, self.terrain, self.own, self.cell_cost, width=4, height=2, bg=COLORS.get(f'{self.color}'))
                sqr.config(command=lambda button = sqr: self.clicking_on_square(button))
                line.append(sqr)
            self.squares.append(line)


    def clicking_on_square(self, pressed_square):
        self.food = pressed_square.food
        self.wood = pressed_square.wood
        self.clay = pressed_square.clay
        self.rock = pressed_square.rock
        self.ore = pressed_square.ore
        self.gold = pressed_square.gold
        self.gem = pressed_square.gem
        self.x = pressed_square.x
        self.y = pressed_square.y
        self.own = pressed_square.own
        self.terrain = pressed_square.terrain
        self.building = pressed_square.building
        self.cell_cost = pressed_square.cell_cost
        game.Update()


    def Building_Pick(self, name):
        self.name = name
        building=all_building.get(name)
        self.message = building[0]
        self.coast_wood = building[1]
        self.coast_rock = building[2]
        self.coast_money = building[3]
        self.l3.config(text=f"Название постройки\n{self.name}\n\nОписание\n{self.message}\n\n\n"
                            f"Дерево = {self.coast_wood}, Камень = {self.coast_rock}\nМонеты = {self.coast_money}")


    def Field_Creation(self):
        menu = tkinter.Menu(self.window)
        self.window.config(menu=menu)
        build_menu = tkinter.Menu(menu, tearoff=0)
        build_menu.add_command(label='Ферма', command = lambda: self.Building_Pick('Ферма'))
        build_menu.add_command(label='Домик лесоруба', command = lambda: self.Building_Pick('Домик лесоруба'))

        trade_menu = tkinter.Menu(menu, tearoff=0)
        trade_menu.add_command(label='Еда')
        menu.add_cascade(label='Строительство', menu=build_menu)
        menu.add_cascade(label='Торговля', menu=trade_menu)


        for i in range(self.ROW):
            for j in range(self.COL):
                sqr=self.squares[i][j]
                sqr.grid(row=i, column=j)
        self.l1 = tkinter.Label(text="Координаты клетки x=x, y=y\nПрирост Еды = 0\nПрирост Дерева = 0\nПрирост Глины = 0\n"
                            "Прирост Камня = 0\nПрирост Руды = 0\nПрирост Золота = 0\nПрирост Самоцветов = 0\n"
                            "Местность = 0\nПостройка = 0\nХозяин = 0", font=FONT, bg=COLORS.get('Silver'), width=27, justify=tkinter.LEFT)
        self.l2 = tkinter.Label(text="Стоимость клетки=x", font=FONT, bg=COLORS.get('Olive'))
        self.l3 = tkinter.Label(text="Название постройки\nПусто\n\nОписание\nПусто\n\n\nДерево = x, Камень = x\n"
                                     "Монеты = x", bg=COLORS.get('Aqua'), width=27, height=10, font=FONT)
        self.l4 = tkinter.Label(text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Камень = {self.res_player.get('rock')}"
                                   f", Монеты = {self.res_player.get('money')}", font=FONT, bg=COLORS.get('Grey'))


        self.b1 = tkinter.Button(text='Купить', command=game.Buying_cell, font=FONT, bg=COLORS.get('Olive'))
        self.b2 = tkinter.Button(text='Купить', command=game.Buying_Building, width=27, font=FONT, bg=COLORS.get('Brown'))
        self.b1.place(x=460, y=111)
        self.b2.place(x=342, y=345)
        self.l1.place(x=342, y=1)
        self.l2.place(x=342, y=112)
        self.l3.place(x=342, y=200)
        self.l4.place(x=0, y=369)


    def Update(self):
        self.l1.config(text=f"Координаты клетки x={self.x}, y={self.y}\nПрирост Еды = {self.food}\nПрирост Дерева = {self.wood}\n"
                            f"Прирост Глины = {self.clay}\nПрирост Камня = {self.rock}\nПрирост Руды = {self.ore}\nПрирост Золота = {self.gold}\n"
                            f"Прирост Самоцветов = {self.gem}\nМестность = {self.terrain}\nПостройка = {self.building}\nХозяин = {self.own}")
        self.l2.config(text=f"Стоимость клетки={self.cell_cost}")
        self.l4.config(text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Камень = {self.res_player.get('rock')}"
                                   f", Монеты = {self.res_player.get('money')}")


    def Buying_cell(self):
        if self.cell_cost != 'x':
            if self.res_player.get('money')>=self.cell_cost and self.own=='Black':
                self.res_player['money'] = self.res_player.get('money') - self.cell_cost
                self.squares[self.x][self.y].Change_Owner(Player_color)
                self.own=Player_color
                game.Update()


    def Buying_Building(self):
        if self.name!='x':
            if self.own==Player_color and self.building=='Пусто' and self.res_player.get('wood')>=self.coast_wood and self.res_player.get('money') >= self.coast_money and self.res_player.get('rock')>=self.coast_rock:
                self.res_player['wood'] = self.res_player.get('wood') - self.coast_wood
                self.res_player['rock'] = self.res_player.get('rock') - self.coast_rock
                self.res_player['money'] = self.res_player.get('money') - self.coast_money
                self.squares[self.x][self.y].Change_Building(self.name)
                self.building = self.name
                game.Update()


    def Trade(self):
        return 1


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
