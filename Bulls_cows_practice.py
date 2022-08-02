from  random import choice                  
s = '0123456789'                                 #create string to choose numbers from (must be 0-9)
x = choice(s)                                    #make first choice and store in x                 
for i in range(3):                               #create 4-time loop to run choosing process until we have a 4-number string
    s = ''.join(j for j in z if j != x[i])       #remove chosen number (equal to x) from s-string to avoid choosing the same one in next interation (nums need to be unique)
    x += choice(s)                               #add chosen number to x-string
n = 0                                            #set attempt counter to zero
while True:
    y = input("Введите четырёхзначное число: ")  #ask for user input
    b = 0; c = 0                                 #define variables for bulls (b) and cows (c) and set counter to zero
    n +=1                                        #increment attempts by 1
    while True: 
        if len(y) != 4:
          print('Число должно быть четырёхзначным, давайте ещё раз!')
          break
        if y[0] == y[1] or y[0] == y[2] or y[0] == y[3] or y[1] == y[2] or y[1] ==y[3] or y[2] == y[3]:
          print('Цифры в числе не должны повторяться. Попробуйте ещё раз.')
        break                                          
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
      
