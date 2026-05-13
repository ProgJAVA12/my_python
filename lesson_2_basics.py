print("Привет я калькулятор финансов!")
print(month := input("Пожалуйста укажи месяц : \n"), month_salary := input("Укажи доходы за этот месяц : \n"),month_expenses := input("Укажи расходы за этот месяц : \n"))
balance = int(month_salary) - float(month_expenses)
percentage_expenses = int(float(month_expenses) / int(month_salary)) * 100
if balance > 0 :
    is_positive = True

else:
    is_positive = False

print(f"""---Ваш финансовый отчет за {month} месяц : 
      
    МЕСЯЦ: {month} 
    ЗАРАБОТАНО: {month_salary}
    РАСХОДЫ: {month_expenses}
    ПРОЦЕНТ РАСХОДОВ: {percentage_expenses}%
    ##########################

    ВАШ ОСТАТОК: {balance}
    ВАШ БАЛАНС ПОЛОЖИТЕЛЬНЫЙ: {is_positive}
    
    Типы переменных: 
    month - {type(month)}
    month_salary - {type(month_salary)}
    month_expenses - {type(month_expenses)}
    balance - {type(balance)}
    is_positive - {type(is_positive)}
    percentage_expenses - {type(percentage_expenses)}
      """)
