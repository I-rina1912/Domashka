""" У вас есть словарь, где ключ - название продукта. Значение - список, который
 содержит цену и кол-во товара.
 Вывести через "-" название - цену- количество.
 С клавиатуры вводите название товара и его кол-во.
 n - выход из программы
 посчитать цену выбранных товаров и сколько  осталось в изначальном списке."""

m = {'Banana': [2, 100],
     'Apple': [1, 50],
     'Peach': [4, 30],
     'Grape': [5, 70]
     }
for key, values in m.items():
    print(key, '-'.join(str(num) for num in values), sep='-')
# # print('Banana', '-', m['Banana'][0], '-', m['Banana'][1])

i = 0
while True:
    p = input('Введите название продукта: ')
    k = int(input('Кол-во продукта: '))
    if p in m:
        print('Продолжайте покупку')
    else:
        print('Такого не существует!')
        p = input('Введите название продукта: ')
    cost = (m[p][0])*k
    print('Цена за', p,  cost, 'ryb')
    i += cost
    print('Общая стоимость', i, 'ryb')
    m[p][1] = (m[p][1]) - k
    # print(m)

    for key, values in m.items():
        print('Остаток',  key, '-'.join(str(num) for num in values), sep='-')
    s = input('Введите n для выхода: ')
    if s == 'n':
        break





