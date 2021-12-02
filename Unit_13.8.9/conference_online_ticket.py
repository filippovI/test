# Цены билетов
price_child = 0
price_young = 990
price_old = 1390

# Количество билетов
tc = None

# Количество билетов с условием ввода только int > 0
while True:
    try:
        tc = int(input("Введите количество билетов, которое хотите приобрести: "))
    except ValueError:
        print("Неверное значение")
    else:
        if tc > 0:
            break
        else:
            print("Неверное значение")

# % скидки
disc = 10 if tc > 3 else 0

# Словарь возраст-стоимость с условием ввода только int > 0
# Изначально ставим цену 990 руб. для категории от 18 до 25
ac = {}
for m in range(tc):
    while True:
        try:
            age = int(input(f"Введите возраст {m + 1} посетителя: "))
            if age > 0:
                ac[age] = price_young
            else:
                print("Неверное значение")
                continue
        except ValueError:
            print("Неверное значение")
        else:
            break

# Цикл сортирует цены по возрасту и выводит сообщение (enumerate/index - для подсчета итераций)
for index, (k, v) in enumerate(ac.items()):
    if k < 18:  # Если возраст < 18 - бесплатно
        ac[k] = price_child
    elif k >= 25:  # Если возраст >=25 - 1390 руб.
        ac[k] = price_old
    print(f"Цена для {index + 1} посетителя возрастом {k} лет - {ac.get(k)} руб.")

# Итоговая сумма с учетом или без учета скидки
print(f"Сумма заказа с учетом скидки {disc}% - " + str(sum(ac.values()) - sum(ac.values()) * disc / 100) + " руб.")

# Для консольки
# program_exit = input("Press enter to exit ")