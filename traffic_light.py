color = input("Какой цвет у световора? \n")
ambulance = input("Есть скорая помощь с сиреной? \n")

if color == "зеленый" and ambulance == "нет":
    print("Можно ехать!")
elif color == "зеленый" and ambulance == "да":
    print("Уступи дорогу спецтранспорту")
elif color == "красный" or color == "желтый":
    print("СТОЙ!!")
elif color != "красный" or color != "зеленый":
    print("Светофор сломан!")
    