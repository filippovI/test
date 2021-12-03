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
                if age in ac.keys():  # Условие для посетителей с одинаковым возрастом
                    ac[age] += 1  # (если уже такой был - ключ остается таким же; значение = значение + 1)
                else:
                    ac[age] = 1
            else:
                print("Неверное значение")
                continue
        except ValueError:
            print("Неверное значение")
        else:
            break

# Цикл сортирует цены по возрасту и выводит сообщение (enumerate/index - для подсчета итераций)
for k, v in ac.items():
    count_people = ac[k]  # Считаем людей одинакового возраста
    if k < 18:      # Если возраст < 18 - бесплатно * на значение количества посетителей
        ac[k] = price_child * ac[k]
    elif k >= 25:   # Если возраст >=25 - 1390 руб. * на значение количества посетителей
        ac[k] = price_old * ac[k]
    else:           # Иначе -  990 руб. * на значение количества посетителей
        ac[k] = price_young * ac[k]
    end = "ей" if count_people % 100 == 11 or count_people % 10 != 1 else "я"  # Если число заканчивается на 11 или не на 1 - окончание "ей"
    print(f"Цена для {count_people} посетител{end} возрастом {k} лет - {ac.get(k)} руб.")

# Итоговая сумма с учетом или без учета скидки
print(f"Сумма заказа с учетом скидки {disc}% - " + str(sum(ac.values()) - sum(ac.values()) * disc / 100) + " руб.")

# Для консоли
# program_exit = input("Press enter to exit ")
