"""
Задача 3:
Даны две строки. Посчитайте сколько раз каждый 
символ первой строки встречается во второй
«one» «onetwonine» - o – 2, n – 3, e – 2
"""
text_1 = input('Введите 1 строку: ')
text_2 = input('Введите 2 строку: ')
# text_1 = 'one'
# text_2 = 'onetwonine'
count = []
simb = []

for i in range(len(text_1)):
    num = 0
    simb.append(text_1[i])
    for j in range(len(text_2)):
        if text_1[i] == text_2[j]:
            num += 1
    count.append(num)
    print(f'{simb[i]} - {count[i]}', end=' ')


