price = int(input("Цена одной тетради (руб.): "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма (руб.): "))

total_cost = price * count
change = paid - total_cost

print(f"Стоимость: {total_cost}")
print(f"Сдача: {change}")
