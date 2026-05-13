all_number = []
number = 7
count = 1
print("""Привет это игра \"УГАДАЙ ЧИСЛО\"!
Правила: 
 -Тебе нужно угадать загаданное число введя его в консоль.
 -Тебе дается 3 попытки.
 -Для выхода из игры отправь 0.
 -В конце игры будет выведена краткая статистика.
      """)
start = input(" Для начала игры отправь \"НАЧАТЬ\" \n Для выхода из игры отправь 0 \n" )
while True:
 
 if start == "начать":
      number_player = input("Введите ваше число : \n")
      all_number.append(number_player)
      if number_player == str(number):
       print(f"Поздравляем !! Ваше число {number_player} - загаданое число {number}")
       print(f"""----Ваша статистика----
загаданое число : 7 
ваши числа : """, end = "")
       for d in all_number:
        print(d, end=" ")
       print(f"\nКоличество попыток: " ,count)
       break
      else:
        print("Попробуй еще раз")
        count = count + 1

 else:   
  print("Игра завершена по желанию пользователя!)")
  break 

      