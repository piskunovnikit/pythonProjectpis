summa_vklada = int(input("введите сумму которую хотите положить на вклад"))


per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb=summa_vklada*per_cent['ТКБ']/100
skb=summa_vklada*per_cent['СКБ']/100
vtb=summa_vklada*per_cent['ВТБ']/100
sber=summa_vklada*per_cent['СБЕР']/100


deposit = [tkb, skb, vtb, sber]
print(deposit)
deposit.sort(reverse = True)
print("Максимальная сумма, которую вы можете заработать-" + str(deposit[0]))