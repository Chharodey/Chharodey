import tkinter
from random import randint
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
    window.geometry("505x430")


    def __init__(self):
        #fail=input('Введите название файла шаблона (Без приписки txt)')
        f = open('Template 1.txt')
        #f = open(f'{fail}.txt')
        strings=f.readlines()
        f.close()
        self.number_turn = 1
        self.number_round = 1
        self.PO = {'Scarlet':0, 'Blue':0}
        self.cell_cost = 'x'
        self.name = 'x'
        self.res_scarlet={'food':0, 'wood':4, 'clay':0, 'rock':0, 'ore':0, 'gold':0, 'gem':0,
                         'plank':0, 'brick':0, 'metal':0, 'furniture':0, 'ceramic':0, 'statue':0, 'instrument':0, 'jewel':0, 'money':1000}
        self.res_blue={'food':0, 'wood':4, 'clay':0, 'rock':0, 'ore':0, 'gold':0, 'gem':0,
                         'plank':0, 'brick':0, 'metal':0, 'furniture':0, 'ceramic':0, 'statue':0, 'instrument':0, 'jewel':0, 'money':20}
        self.squares=[]
        self.ROW=len(strings)
        self.COL=len(strings[1])-1
        for i in range(self.ROW):
            line=[]
            for j in range(self.COL):
                self.fg = 'White'
                self.own = 'White'
                self.food = 0
                self.wood = 0
                self.clay = 0
                self.rock = 0
                self.ore = 0
                self.gold = 0
                self.gem = 0
                difference = abs(i-j)
                self.cell_cost = ((self.COL-1)-difference)
                if strings[i][j] == 'F':
                    self.color = 'Olive'
                    self.food = randint(1, 3)
                    self.wood = randint(2, 6)
                    self.clay = randint(0, 1)
                    self.rock = randint(0, 2)
                    self.terrain = 'Лес'
                elif strings[i][j] == 'M':
                    self.color = 'Grey'
                    self.food = randint(0, 2)
                    self.wood = randint(0, 3)
                    self.rock = randint(3, 6)
                    self.ore = randint(1, 3)
                    a = randint(1, 10)
                    if a < 5:
                        self.gold = 1
                    elif a == 5:
                        self.gold = 2
                    a=randint(1, 10)
                    if a==1:
                        self.gem = 1
                    self.terrain = 'Горы'
                elif strings[i][j] == 'G':
                    self.color = 'Green'
                    self.food = randint(2, 5)
                    self.clay = randint(0, 1)
                    self.wood = randint(1, 2)
                    self.rock = randint(0, 1)
                    self.terrain = 'Луг'
                elif strings[i][j] == 'H':
                    self.color = 'Brown'
                    self.food = randint(2, 4)
                    self.clay = randint(2, 4)
                    self.wood = randint(1, 3)
                    self.rock = randint(0, 2)
                    self.terrain = 'Холм'
                elif strings[i][j] == 'R':
                    self.color = 'Aqua'
                    self.clay = randint(3, 7)
                    a = randint(1, 100)
                    if a < 21:
                        self.gold = 1
                    a = randint(1, 100)
                    if a < 6:
                        self.gem = 2
                    elif a < 26:
                        self.gem = 1
                    self.terrain = 'Река'
                elif (strings[i][j] == 'S') or (strings[i][j] == 'B'):
                    self.color = 'Silver'
                    self.terrain = 'Крепость'
                    if strings[i][j] == 'S':
                        self.own = 'Scarlet'
                        self.fg = 'Scarlet'
                    else:
                        self.own = 'Blue'
                        self.fg = 'Blue'

                sqr=Cell(Playing_Field.window, i, j, self.food, self.wood, self.clay, self.rock, self.ore, self.gold, self.gem, self.terrain, self.own, self.cell_cost, text='*', width=4, height=2, fg=COLORS.get(f'{self.fg}'), bg=COLORS.get(f'{self.color}'))
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
        self.Update()


    def Building_Pick(self, name):
        self.name = name
        building=all_building.get(name)
        self.type_terrain=building[0]
        self.read_terrain = ''
        for i in self.type_terrain:
            self.read_terrain+=i+'  '
        self.message = building[1]
        self.coast_wood = building[2]
        self.coast_rock = building[3]
        self.coast_plank = building[4]
        self.coast_brick = building[5]
        self.coast_instr = building[6]
        self.coast_money = building[7]
        self.l3.config(text=f"Название постройки\n{self.name}\n\nВозможная местность\n{self.read_terrain}\n\nОписание\n{self.message}\n\n"
                            f"Дерево = {self.coast_wood}, Камень = {self.coast_rock}\nДоски = {self.coast_plank}, Кирпичи = {self.coast_brick}\nИнструменты = {self.coast_instr}\nМонеты = {self.coast_money}")


    def Field_Creation(self):
        menu = tkinter.Menu(self.window)
        self.window.config(menu=menu)
        build_menu = tkinter.Menu(menu, tearoff=0)

        build_menu1 = tkinter.Menu(menu, tearoff=0)
        build_menu1.add_command(label='Ферма', command=lambda: self.Building_Pick('Ферма'))
        build_menu1.add_command(label='Лесоруб', command=lambda: self.Building_Pick('Лесоруб'))
        build_menu1.add_command(label='Карьер', command=lambda: self.Building_Pick('Карьер'))
        build_menu1.add_command(label='Шахта', command=lambda: self.Building_Pick('Шахта'))
        build_menu1.add_command(label='Рыбак', command=lambda: self.Building_Pick('Рыбак'))
        build_menu1.add_command(label='Ловцы жемчуга', command=lambda: self.Building_Pick('Ловцы жемчуга'))

        build_menu2 = tkinter.Menu(menu, tearoff=0)
        build_menu2.add_command(label='Мельница', command=lambda: self.Building_Pick('Мельница'))
        build_menu2.add_command(label='Лесопилка', command=lambda: self.Building_Pick('Лесопилка'))
        build_menu2.add_command(label='Каменоломня', command=lambda: self.Building_Pick('Каменоломня'))
        build_menu2.add_command(label='Прииск', command=lambda: self.Building_Pick('Прииск'))

        build_menu3 = tkinter.Menu(menu, tearoff=0)
        build_menu3.add_command(label='Столяр', command=lambda: self.Building_Pick('Столяр'))
        build_menu3.add_command(label='Печь для обжига', command=lambda: self.Building_Pick('Печь для обжига'))
        build_menu3.add_command(label='Плавильня', command=lambda: self.Building_Pick('Плавильня'))
        build_menu3.add_command(label='Монетный двор', command=lambda: self.Building_Pick('Монетный двор'))

        build_menu4 = tkinter.Menu(menu, tearoff=0)
        build_menu4.add_command(label='Мебельщик', command=lambda: self.Building_Pick('Мебельщик'))
        build_menu4.add_command(label='Гончар', command=lambda: self.Building_Pick('Гончар'))
        build_menu4.add_command(label='Скульптор', command=lambda: self.Building_Pick('Скульптор'))
        build_menu4.add_command(label='Кузнец', command=lambda: self.Building_Pick('Кузнец'))
        build_menu4.add_command(label='Ювелир', command=lambda: self.Building_Pick('Ювелир'))

        build_menu5 = tkinter.Menu(menu, tearoff=0)
        build_menu5.add_command(label='Банк', command=lambda: self.Building_Pick('Банк'))

        build_menu.add_cascade(label='Базовая добыча', menu=build_menu1)
        build_menu.add_cascade(label='Продвинутая добыча', menu=build_menu2)
        build_menu.add_cascade(label='Базовая обработка', menu=build_menu3)
        build_menu.add_cascade(label='Продвинутая обработка', menu=build_menu4)
        build_menu.add_cascade(label='Крепость', menu=build_menu5)
        build_menu.add_command(label='Снести здание', command=self.Break_Building)

        trade_menu = tkinter.Menu(menu, tearoff=0)

        trade_menu1 = tkinter.Menu(menu, tearoff=0)
        trade_menu1.add_command(label='Дерево (2)', command=lambda: self.Trade('Buy', 'wood', 2))
        trade_menu1.add_command(label='Камень (2)', command=lambda: self.Trade('Buy', 'rock', 2))
        trade_menu1.add_command(label='Доски (3)', command=lambda: self.Trade('Buy', 'plank', 3))
        trade_menu1.add_command(label='Кирпичи (1.5)', command=lambda: self.Trade('Buy', 'brick', 1.5))
        trade_menu1.add_command(label='Инструменты (5)', command=lambda: self.Trade('Buy', 'instrument', 5))

        trade_menu2 = tkinter.Menu(menu, tearoff=0)
        trade_menu2.add_command(label='Еда (1)', command=lambda: self.Trade('Sell', 'food', 1))
        trade_menu2.add_command(label='Дерево (1)', command=lambda: self.Trade('Sell', 'wood', 1))
        trade_menu2.add_command(label='Камень (1)', command=lambda: self.Trade('Sell', 'rock', 1))
        trade_menu2.add_command(label='Самоцветы (3)', command=lambda: self.Trade('Sell', 'gem', 3))
        trade_menu2.add_command(label='Доски (1.5)', command=lambda: self.Trade('Sell', 'plank', 1.5))
        trade_menu2.add_command(label='Кирпичи (0.5)', command=lambda: self.Trade('Sell', 'brick', 0.5))
        trade_menu2.add_command(label='Металл (2)', command=lambda: self.Trade('Sell', 'metal', 2))
        trade_menu2.add_command(label='Мебель (4)', command=lambda: self.Trade('Sell', 'furniture', 4))
        trade_menu2.add_command(label='Керамика (1)', command=lambda: self.Trade('Sell', 'ceramic', 1))
        trade_menu2.add_command(label='Статуя (5)', command=lambda: self.Trade('Sell', 'statue', 5))
        trade_menu2.add_command(label='Инструменты (3)', command=lambda: self.Trade('Sell', 'instrument', 3))
        trade_menu2.add_command(label='Драгоценности (6)', command=lambda: self.Trade('Sell', 'jewel', 6))

        trade_menu.add_cascade(label='Покупка', menu=trade_menu1)
        trade_menu.add_cascade(label='Продажа', menu=trade_menu2)

        menu.add_cascade(label='Строительство', menu=build_menu)
        menu.add_cascade(label='Торговля', menu=trade_menu)
        menu.add_command(label='Закончить ход', command=self.End_Turn)


        for i in range(self.ROW):
            for j in range(self.COL):
                sqr=self.squares[i][j]
                sqr.grid(row=i, column=j)
        self.l1 = tkinter.Label(text="Координаты клетки x=x, y=y\nПрирост Еды = 0\nПрирост Дерева = 0\nПрирост Глины = 0\n"
                            "Прирост Камня = 0\nПрирост Руды = 0\nПрирост Золота = 0\nПрирост Самоцветов = 0\n"
                            "Местность = 0\nПостройка = 0\nХозяин = 0", font=FONT, bg=COLORS.get('Silver'), width=27, justify=tkinter.LEFT)
        self.l2 = tkinter.Label(text="Стоимость клетки=x", font=FONT, width=19, bg=COLORS.get('Olive'))
        self.l3 = tkinter.Label(text=f"Название постройки\nПусто\n\nВозможная местность\nПусто\n\nОписание\nПусто\n\n"
                                     f"Дерево = х, Камень = х\nДоски = х, Кирпичи = х\nИнструменты = х\nМонеты = х", bg=COLORS.get('S_field'), width=27, height=15, font=FONT)
        self.l4 = tkinter.Label(text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Глина = {self.res_player.get('clay')}, Камень = {self.res_player.get('rock')}"
                                   f", Руда = {self.res_player.get('ore')}\nЗолото = {self.res_player.get('gold')}, Самоцветы = {self.res_player.get('gem')}, Доски = {self.res_player.get('plank')}"
                                     f", Кирпичи = {self.res_player.get('brick')}\nМеталл = {self.res_player.get('metal')}, Мебель = {self.res_player.get('furniture')}, "
                                     f"Керамика = {self.res_player.get('ceramic')}, Статуи = {self.res_player.get('statue')}\nИнструменты = {self.res_player.get('instrument')}, "
                                     f"Драгоценности = {self.res_player.get('jewel')}, Монеты = {self.res_player.get('money')}", width=56, font=FONT, bg=COLORS.get('Grey'))


        self.b1 = tkinter.Button(text='Купить', command=self.Buying_cell, font=FONT, bg=COLORS.get('Olive'))
        self.b2 = tkinter.Button(text='Купить', command=self.Buying_Building, width=27, height=3, font=FONT, bg=COLORS.get('Brown'))
        self.b1.place(x=460, y=160)
        self.b2.place(x=342, y=386)
        self.l1.place(x=342, y=1)
        self.l2.place(x=342, y=161)
        self.l3.place(x=342, y=180)
        self.l4.place(x=0, y=369)


    def Update(self):
        self.l1.config(text=f"Координаты клетки x={self.x}, y={self.y}\nПрирост Еды = {self.food}\nПрирост Дерева = {self.wood}\n"
                            f"Прирост Глины = {self.clay}\nПрирост Камня = {self.rock}\nПрирост Руды = {self.ore}\nПрирост Золота = {self.gold}\n"
                            f"Прирост Самоцветов = {self.gem}\nМестность = {self.terrain}\nПостройка = {self.building}\nХозяин = {COLORS_READ.get(self.own)}")
        self.l2.config(text=f"Стоимость клетки={self.cell_cost}")
        self.Update_res()


    def Update_res(self):
        self.l4.config(
            text=f"Еда = {self.res_player.get('food')}, Дерево = {self.res_player.get('wood')}, Глина = {self.res_player.get('clay')}, Камень = {self.res_player.get('rock')}"
                 f", Руда = {self.res_player.get('ore')}\nЗолото = {self.res_player.get('gold')}, Самоцветы = {self.res_player.get('gem')}, Доски = {self.res_player.get('plank')}"
                 f", Кирпичи = {self.res_player.get('brick')}\nМеталл = {self.res_player.get('metal')}, Мебель = {self.res_player.get('furniture')}, "
                 f"Керамика = {self.res_player.get('ceramic')}, Статуи = {self.res_player.get('statue')}\nИнструменты = {self.res_player.get('instrument')}, "
                 f"Драгоценности = {self.res_player.get('jewel')}, Монеты = {self.res_player.get('money')}")


    def Buying_cell(self):
        if self.cell_cost != 'x':
            self.test = 0
            if self.x!=8:
                if self.squares[self.x+1][self.y].own==self.Player_color:
                    self.test=1
            if self.x!=0:
                if self.squares[self.x-1][self.y].own==self.Player_color:
                    self.test=1
            if self.y!=0:
                if self.squares[self.x][self.y-1].own==self.Player_color:
                    self.test=1
            if self.y!=8:
                if self.squares[self.x][self.y+1].own==self.Player_color:
                    self.test=1
            if  self.test==1:
                if self.res_player.get('money')>=self.cell_cost and self.own=='White':
                    self.res_player['money'] = self.res_player.get('money') - self.cell_cost
                    self.squares[self.x][self.y].Change_Owner(self.Player_color)
                    self.own=self.Player_color
                    self.squares[self.x][self.y].config(fg = COLORS.get(f'{self.Player_color}'))
                    self.Update()


    def Buying_Building(self):
        if self.name!='x':
            if self.own==self.Player_color and self.building == 'Пусто' and self.res_player.get('wood') >= self.coast_wood and self.res_player.get('money') >= self.coast_money and self.res_player.get('rock') >= self.coast_rock\
                    and self.res_player.get('plank') >= self.coast_plank and self.res_player.get('brick') >= self.coast_brick and self.res_player.get('instrument') >= self.coast_instr and self.terrain in self.type_terrain:
                self.res_player['wood'] = self.res_player.get('wood') - self.coast_wood
                self.res_player['rock'] = self.res_player.get('rock') - self.coast_rock
                self.res_player['plank'] = self.res_player.get('plank') - self.coast_plank
                self.res_player['brick'] = self.res_player.get('brick') - self.coast_brick
                self.res_player['instrument'] = self.res_player.get('instrument') - self.coast_instr
                self.res_player['money'] = self.res_player.get('money') - self.coast_money
                self.squares[self.x][self.y].Change_Building(self.name)
                self.building = self.name
                self.Update()


    def Break_Building(self):
        if self.own==self.Player_color and self.building != 'Пусто':
            building = all_building.get(self.building)
            self.res_player['wood'] += building[2]/2
            self.res_player['rock'] += building[3]/2
            self.res_player['plank'] += building[4]/2
            self.res_player['brick'] += building[5]/2
            self.res_player['instrument'] += building[6]/2
            self.res_player['money'] += building[7]/2


            self.squares[self.x][self.y].Change_Building('Пусто')
            self.building = 'Пусто'
            self.Update()


    def Trade(self, operation, res, price):
        if operation == 'Buy' and self.res_player.get('money') >= price:
            self.res_player[res] += 1
            self.res_player['money'] -= price
        elif operation == 'Sell' and self.res_player.get(res) >= 1:
            self.res_player[res] -= 1
            self.res_player['money'] += price
        self.Update_res()


    def End_Turn(self):
        self.number_turn+=1
        self.Production()
        if self.Player_color=='Scarlet':
            for i in all_res:
                self.res_scarlet[i]=self.res_player.get(i)
            self.res_player = self.res_blue
            self.Player_color = 'Blue'
            self.l3.config(bg=COLORS.get('B_field'))
        elif self.Player_color=='Blue':
            for i in all_res:
                self.res_blue[i]=self.res_player.get(i)
            self.res_player = self.res_scarlet
            self.Player_color = 'Scarlet'
            self.l3.config(bg=COLORS.get('S_field'))
        if self.number_turn == 3:
            self.End_Round()
        self.Update_res()


    def End_Round(self):
        self.number_round+=1
        self.number_turn=1

        if self.number_round == 13:
            print('Game over')


    def Production(self):
        self.new_res = {'food': 0, 'wood': 0, 'clay': 0, 'rock': 0, 'ore': 0, 'gold': 0, 'gem': 0, 'plank': 0,
                        'brick': 0, 'metal': 0, 'furniture': 0, 'ceramic': 0, 'statue': 0, 'instrument': 0, 'jewel': 0,
                        'money': 0, 'gold_money': 0}
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.squares[i][j].own == self.Player_color and self.squares[i][j].terrain != 'Крепость':
                    Build = self.squares[i][j].building
                    if Build != 'Пусто':
                        self.new_res['food'] -= 1
                        if Build == 'Ферма':
                            self.new_res['food'] += self.squares[i][j].food + 1
                        elif Build == 'Лесоруб':
                            self.new_res['wood'] += self.squares[i][j].wood
                        elif Build == 'Карьер':
                            self.new_res['rock'] += self.squares[i][j].rock
                            self.new_res['clay'] += self.squares[i][j].clay
                        elif Build == 'Шахта':
                            self.new_res['ore'] += self.squares[i][j].ore
                            self.new_res['gold'] += self.squares[i][j].gold
                            self.new_res['gem'] += self.squares[i][j].gem
                        elif Build == 'Рыбак':
                            self.new_res['food'] += 4 + 1
                        elif Build == 'Ловцы жемчуга':
                            self.new_res['gold'] += self.squares[i][j].gold
                            self.new_res['gem'] += self.squares[i][j].gem
                        elif Build == 'Мельница':
                            self.new_res['food'] += self.squares[i][j].food * 1.5 + 1
                        elif Build == 'Лесопилка':
                            self.new_res['wood'] += self.squares[i][j].wood * 1.5
                        elif Build == 'Каменоломня':
                            self.new_res['rock'] += self.squares[i][j].rock * 1.5
                        elif Build == 'Прииск':
                            self.new_res['gold'] += self.squares[i][j].gold * 1.5
                            self.new_res['gem'] += self.squares[i][j].gem * 1.5
                        elif Build == 'Столяр':
                            self.new_res['plank'] += 4
                        elif Build == 'Печь для обжига':
                            self.new_res['brick'] += 4
                        elif Build == 'Плавильня':
                            self.new_res['metal'] += 3
                        elif Build == 'Монетный двор':
                            self.new_res['gold_money'] += 3
                        elif Build == 'Мебельщик':
                            self.new_res['furniture'] += 2
                        elif Build == 'Гончар':
                            self.new_res['ceramic'] += 3
                        elif Build == 'Скульптор':
                            self.new_res['statue'] += 1
                        elif Build == 'Кузнец':
                            self.new_res['instrument'] += 4
                        elif Build == 'Ювелир':
                            self.new_res['jewel'] += 4
                    else:
                        self.new_res['money'] -= 1
        for i in ['food', 'wood', 'clay', 'rock', 'ore', 'gold', 'gem', 'money']:
            self.res_player[i] += self.new_res.get(i)

        self.Basic_Recycling('wood', 'plank', 1)
        self.Basic_Recycling('clay', 'brick', 1)
        self.Advanced_Recycling('wood', 'ore', 'metal', 0.5, 1)
        self.Basic_Recycling('plank', 'furniture', 2)
        self.Basic_Recycling('clay', 'ceramic', 1)
        self.Basic_Recycling('rock', 'statue', 3)
        self.Advanced_Recycling('wood', 'metal', 'instrument', 0.5, 1)
        self.Advanced_Recycling('gem', 'gold', 'jewel', 0.5, 1)

        while (self.res_player.get('gold') >= 1) and (self.new_res.get('gold_money')>0):
            self.res_player['gold'] -= 1
            self.res_player['money'] += 4

        if self.res_player.get('food')<0:
            self.PO[self.Player_color]+=self.res_player.get('food')
            self.res_player['food']=0

        if self.res_player.get('money')<0:
            self.PO[self.Player_color]+=self.res_player.get('money')
            self.res_player['money']=0



    def Basic_Recycling(self, res1, res3, coefficient1):
        while (self.res_player.get(res1)>= coefficient1) and (self.new_res.get(res3)>0):
            self.res_player[res1] -= coefficient1
            self.res_player[res3] += 1

    def Advanced_Recycling(self, res1, res2, res3, coefficient1, coefficient2):
        while (self.res_player.get(res1) >= coefficient1) and (self.new_res.get(res3) > 0)\
                and (self.res_player.get(res2) >= coefficient2):
            self.res_player[res1] -= coefficient1
            self.res_player[res2] -= coefficient2
            self.res_player[res3] += 1



    def Start(self):
        self.Player_color = 'Scarlet'
        self.res_player = self.res_scarlet
        self.Field_Creation()
        Playing_Field.window.mainloop()


game = Playing_Field()
game.Start()
