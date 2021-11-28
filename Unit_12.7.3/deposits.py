per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую хотите внести: "))
per_cent['ТКБ'] = money * per_cent.get('ТКБ') / 100
per_cent['СКБ'] = money * per_cent.get('СКБ') / 100
per_cent['ВТБ'] = money * per_cent.get('ВТБ') / 100
per_cent['СБЕР'] = money * per_cent.get('СБЕР') / 100
per_cent = {k: round(v, 2) for k, v in per_cent.items()}
for k, v in per_cent.items():
    print(k, '-', v)
print('Максимальная сумма, которую вы можете заработать - ' + str(max(per_cent.values())))
# Для консольки
# program_exit = input("Press enter to exit ")
