product_dataBase = {"яблоко": 52, "груша" : 54, "банан" : 50}
all_calories = []

def calculate_calories(weight, calories_per_100g): 
        result = (weight / 100) * calories_per_100g
        return result

print(f"Привет я умный калькуляор калорий")
while True:
      

      product = input("что ты сьел?")
      if product.lower() == "exit" :
       break
      if product in product_dataBase:
             weight = float(input("какой вес"))
             result = calculate_calories(weight, product_dataBase[product])
             all_calories.append({"name" : product, "calories": result})
             print(f"добавили в список {product} - {result} Ккал")
      else :
        weight = float(input ("Продукта нет в базе, введите вес"))
        calories = float(input("Введите калории"))
        product_dataBase[product] = calories
        result = calculate_calories(weight, calories)
        print(f"добавили в список {product} - {result} Ккал")
        all_calories.append({"name" : product, "calories": result})


print(f"\n---Ваш отчет за день---")

for entry in all_calories:
     print(f"*{entry['name']} : {entry['calories']} Ккал")
total = sum(d['calories'] for d in all_calories)
print(f"Общее количество каллорий сегодня - {total} Ккалл")
       

