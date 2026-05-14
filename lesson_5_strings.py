print("Здравствуйте я генератор случайных отчетов!")

name = input(f"Пожалуйста введите ваше имя : \n")

name = name.capitalize().strip()

product_name = input(f"Пожалуйста введите название товара : \n")

product_name = product_name.upper().strip()

price_product = float(input(f"Пожалуйста введите цену товара : \n"))

count_product = float(input(f"Пожалуйста введите количество товара : \n"))

price = price_product * count_product

print(f" МЕНЕДЖЕР : [{name}] \n " + 
f"ЗАКАЗ : [{product_name}] \n " +
"==" * 10 + "\n" +
f" ИТОГОВАЯ СТОИМОСТЬ : [{price:.2f}] рублей. \n"
f" Длина строки с названием товара : {len(product_name)}")

