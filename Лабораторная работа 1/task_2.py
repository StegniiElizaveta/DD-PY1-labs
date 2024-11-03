# TODO Найдите количество книг, которое можно разместить на дискете
memory_in_megabytes = 1.44
memory_for_one_book_in_bytes = 100 * 50 * 25 * 4
memory_for_one_book_in_megabytes = memory_for_one_book_in_bytes / ( 1024 * 1024 )
books = int(memory_in_megabytes // memory_for_one_book_in_megabytes)
print("Количество книг, помещающихся на дискету:", books)
# Я надеюсь, это можно не считать за «магические» числа, потому что тут из
# условия всё понятно и с сотней переменных будет еще запутанней
