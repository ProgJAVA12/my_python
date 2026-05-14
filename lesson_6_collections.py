todo_list = ["купить хлеб", "помыть машину"]
new_task = input("Введите новую задачу для добавления : \n")
todo_list.append(new_task)
print(f"Вторая задача из списка : {todo_list[1]}")
project_alfa = ("Проект Альфа", "14.02.2027")
#project_alfa[0] = "новое имя" - Ошибка python 'Объект не поддерживает присваивание элементов'
task_status = {"купить хлеб" : "выполнено", "помыть машину" : "в процессе"}
task_status[f"{new_task}"] = "новая"
for key,vault in task_status.items() :
    print(f"{key,vault}")
status_tag = ["работа","личное","работа","домашнее"]
status_tags = set(status_tag)


for item in status_tags :
    print(item,end=" ")