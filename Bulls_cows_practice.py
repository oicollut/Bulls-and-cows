from  random import choice                  
s = '0123456789'                                 #create string to choose numbers from (must be 0-9)
x = choice(s)                                    #make first choice and store in x                 
for i in range(3):                               #create 3-time loop to run choosing process until we have a 4-number string
    s = ''.join(j for j in z if j != x[i])       #remove chosen number (equal to x) from s-string to avoid choosing the same one in next interation (nums need to be unique)
    x += choice(s)                               #add chosen number to x-string
n = 0                                            #set attempt counter to zero
while True:                                      #infinite cycle to continue asking for number (breaks when bulls=4, player wins)
    y = input("Введите четырёхзначное число: ")  #ask for user input
    b = 0; c = 0                                 #define variables for bulls (b) and cows (c) and set counter to zero
    n +=1                                        #increment attempts by 1
    while True:                                  #while loop to catch invalid input
        if len(y) != 4:                          #catch wrong number of digits
          print('Число должно быть четырёхзначным, давайте ещё раз!')
          break
        if y[0] == y[1] or y[0] == y[2] or y[0] == y[3] or y[1] == y[2] or y[1] ==y[3] or y[2] == y[3]: #catch numbers with repeating digits
          print('Цифры в числе не должны повторяться. Попробуйте ещё раз.')
        break                                          
    for i in range(4):                           #loop to compare input number with computer-generated number 4 times                              
      if x[i] == y[i]:                           #matching digit in matching position is a bull
          b += 1                                 #increment number of bulls
      elif y[i] in x:                            #matching digit in different position is a cow
           c += 1                                #increment number of cows
     cow = 'коров'                               #create string with cow word 'base'
     bull = 'бык'                                #create string with bull workd 'base'
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
      
