deposit = []
per_cent = {'Ткб': 5.6, 'Скб': 5.9, 'Втб': 4.28, 'Сбер': 4.0}
money = int(input('Введите сумму:'))
deposit.append(per_cent['Ткб']*money/100)
deposit.append(per_cent['Скб']*money/100)
deposit.append(per_cent['Втб']*money/100)
deposit.append(per_cent['Сбер']*money/100)
print('Годовой процент:', deposit)
print("Максимальная сумма - ", max(deposit))