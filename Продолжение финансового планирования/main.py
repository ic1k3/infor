salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
o_deficit = 0
tek_spend = spend
for month in range(1, months + 1):
    if month > 1:
        tek_spend *= (1 + increase)
    deficit = max(0, tek_spend - salary)
    o_deficit += deficit
money = round(o_deficit)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money}")
