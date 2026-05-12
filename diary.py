all_calories = []

print("Привет я дневник продуктов на день")
print("какие продукты ты сегодня сьел?")
while True:
     object = input("что ты сьел?")
     if object =="exit":
      break

     weight = float(input("вес продукта"))
     calories_per_100g = float(input("сколько калорий"))
     result = (weight / 100) * calories_per_100g
     all_calories.append(result)
     print(f"добавили в список {object} - {result} Ккал")


total = sum(all_calories)

print(f"Всего за день калорий : {total} Ккал")

       