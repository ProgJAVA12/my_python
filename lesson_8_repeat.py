orders = {"Иван": 5000, "Мария": 5000, "Игорь": 750}
while True:
    name = input("Введите имя клиента : \n")
    name = name.capitalize().strip()
    if name.lower() == "стоп" or name.lower() == "stop":
        break
    else:
        order_total = input("Введите сумму заказа : \n")
        if order_total.lower() == "стоп" or order_total.lower() == "stop":
            break
        else:
            order_total = float(order_total)
            orders[name] = order_total
        # print("код продолжается")


bought_categories = ["Электроника", "Книги", "Электроника", "Одежда", "Книги"]
bought_categories = set(bought_categories)
count_num = 0
total_elements = len(bought_categories)
for item in bought_categories:
    count_num += 1
    if count_num == total_elements:
        print(item)
    else:
        print(item, end=", ")

for name, amount in orders.items():
    if amount >= 5000 and name == "Иван":
        print(f"{name} Вам доступна VIP ДОСТАВКА")
    elif amount <= 500 and name != "ADMIN":
        print(f"{name}Минимальная сумма заказа 501 рубль. Добавьте товары!")
    else:
        print(f"Заказ для {name} на сумму : {amount:2.f} руб. успешно оформлен")
