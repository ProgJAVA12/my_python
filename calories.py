print("Привет я калькулятор калорий!")
print("Пожалуйста введи необходимые данные :")
object = input("что ты сьел?")
weight = float(input("Вес продукта?"))
calories_per_100g = float(input("сколько калорий на 100г?"))
calories = (weight/100)*calories_per_100g
if calories >= 2000:
    print("Осторожно это много")
elif calories <= 500: 
    print("Можно сьесть что нибудь еще")

else : print("Приятного аппетита")