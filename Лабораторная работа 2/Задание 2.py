salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
months1 = 10
increase = 0.03  # Ежемесячный рост цен
debt = 0
money_capital = 0

while months != 0:
    debt = salary - spend
    debt = debt/-1
    money_capital = money_capital + debt
    months -= 1
    if months < 10:
        spend = (spend * increase) + spend

money_capital = int(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months1} месяцев без долгов:", money_capital)
