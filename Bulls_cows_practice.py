import re
from  random import choice                  # Импортируем функцию choice из библиотеки random
z = '0123456789'                            # Создаём строку z
x = choice(z[1:10])                         # Создаём строку x из одного случайно выбранного символа из среза строки z (без 0)
for i in range(3):                          # В цикле из 3-x повторений
    z = ''.join(j for j in z if j != x[i])  # удаляем из строки z символ который добавили в строку x,
    x += choice(z)                           # добавляем к строке x случайно выбранные символы из строки z.  
n = 0                                 
while True:
    y = input("Введите четырёхзначное число: ") # Функция ввода строки
    b = 0; c = 0                                # Создаём переменные Bulls и Cows
    n +=1
    while True: 
        if len(y) != 4:
          print('Число должно быть четырёхзначным, давайте ещё раз!')
          break
        if y[0] == y[1] or y[0] == y[2] or y[0] == y[3] or y[1] == y[2] or y[1] ==y[3] or y[2] == y[3]:
          print('Цифры в числе не должны повторяться. Попробуйте ещё раз.')
        break                                        #прибавляем 1 к счетчику ходов   
    for i in range(4):        
      cow = 'коров' 
      bull = 'бык'                         
      if x[i] == y[i]:                        
          b += 1                              
      elif y[i] in x:                        
           c += 1 
      if b==0:
          bull = bull + 'ов'
      if b >= 2:
           bull = bull + 'a'
      if c==1:
        cow = cow + 'a'
      if c > 1:
          cow = cow + 'ы'
    print('В числе ' + y + ' ' + str(b) + ' ' + bull +  ' ' + str(c) +  ' ' + cow)
    if b==4:
          if n == 0:
            print('Вот это удача! Вы победили за ', n, " ход!")
          if n > 3 and n < 21:
             print('Поздравляю! Вы победили за ', n, " ходов!")
          if n == 21 or n == 31 or n == 41 or n == 51 or n == 61:
            print('Наконец-то! Вы победили за ', n, " ход!")
          if n > 21 and n < 25 or n > 31 and n < 35 or n > 41 and n < 45 or n > 51  and n < 55 or n > 61 and n < 65:
            print('Поздравляю! Вы победили за ', n, " хода!")
          else:
             print('Наконец-то! Вы победили за ', n, " ходов!")
          break
      