def count_letters(text):
    lowercase_text = text.lower()
    #теперь нам нужно получить словарь, в котором идёт буква - кол-во
    list_ = []
    for i in lowercase_text:
        if i.isalpha():
            list_.append(i)
    unique_list_ = []
    for i in list_:
        if i not in unique_list_:
            unique_list_.append(i)
    # теперь у нас есть список со всеми буквами и список с уникальными
    dictionary = {}
    for letter in unique_list_:
        count = 0
        for i in list_:
            if i == letter:
                count += 1
        dictionary[letter] = count
    return dictionary

#Тестируем эту штуку
#text = 'Чё-та я длинное написала, но должно работать...'
#print(count_letters(text))
#Штука работает корректно

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary):
    #надо достать все values и просуммировать
    dict_of_frequencies = {}
    denominator = sum(dictionary.values())
    for key, value in dictionary.items():
        dict_of_frequencies[key] = f"{value/denominator:.2f}"
    return dict_of_frequencies

#Тестируем теперь эту штуку
#text = 'Чё-та я длинное написала, но должно работать...'
#for letter, freq in calculate_frequency(count_letters(text)).items():
#    print(f'{letter}: {freq}')
#Штука работает корректно

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
for letter, freq in calculate_frequency(count_letters(main_str)).items():
    print(f'{letter}: {freq}')
#print(count_letters(main_str))
# TODO Распечатайте в столбик букву и её частоту в тексте

