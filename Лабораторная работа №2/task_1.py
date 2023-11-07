money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0

while True:
    diff = spend - salary # определяем ежемесячную разницу трат и дохода
    if diff > money_capital: # действие прекратится когда разница будет больше фин подушки
        break

    month += 1 # Прибавляем месяц
    money_capital -= diff # Вычитаем разницу из фин подушки
    spend *= (1 + increase) # Траты растут на 5%

print("Количество месяцев, которое можно протянуть без долгов:", month)
