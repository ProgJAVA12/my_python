
print(f"Добро пожаловать в бункер!")
name = input("Пожалуйста введите Ваше имя: \n")
age  = input("Пожалуйста введите ваш возраст: \n")
password = input("Ввеедите пароль: \n")

can_enter = (name.lower() == "admin") and (int(age) >= 18) and (password.lower() == "python31")

if not(int(age) <= 100):
    print("Вы слишком мудры для этого бункера ХD")

if can_enter == True:
    print(f"Доступ разрешен! Добро пожаловать {name}")
else:
    print("!!В доступе отказано!!")
