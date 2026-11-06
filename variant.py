total = int(input("Общее количество студентов: "))
capacity = int(input("Мест в автобусе: "))

full_buses = total // capacity
remainder = total % capacity
total_buses = (total + capacity - 1) // capacity

print(f"Полностью заполненных автобусов: {full_buses}")
print(f"Остаток студентов: {remainder}")
print(f"Минимальное число автобусов: {total_buses}")
