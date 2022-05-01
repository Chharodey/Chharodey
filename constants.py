COLORS={'Olive':'#808000', 'Green':'#008000', 'Grey':'#808080', 'Aqua':'#00FFFF', 'Silver':'#C0C0C0' ,
        'Brown':'#C45824', 'Yellow':'#FFFF00', 'Blue':'#0000FF'}
FONT='Tumes 8'
STANDART=['Лес', 'Горы', 'Луг', 'Холм']
all_building={'Ферма':[STANDART, 'Добывает из клетки еду',10,10,10,10,10,10], 'Домик лесоруба':[STANDART, 'Добывает из клетки дерево',1,1,1], 'Карьер':[['Лес', 'Горы', 'Луг', 'Холм', 'Река'], 'Добывает из клетки камень и глину',1,3,5],
              'Шахта':[STANDART, 'Добывает из клетки руду, золото и драгоценности',1,1,1]}
all_res=['food', 'wood', 'clay', 'rock', 'ore', 'gold', 'gem', 'plank', 'brick', 'metal', 'furniture', 'ceramic', 'statue', 'instrument', 'jewel', 'money']