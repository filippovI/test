per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую хотите внести: "))
for k, v in per_cent.items():
    per_cent[k] = round(money * per_cent.get(k) / 100, 2)
    print(k, '-', per_cent.get(k))
print('Максимальная сумма, которую вы можете заработать - ' + str(max(per_cent.values())))
# Для консольки
program_exit = input("Press enter to exit ")
