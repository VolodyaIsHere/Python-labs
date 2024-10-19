# TODO Найдите количество книг, которое можно разместить на дискете


pages_in_book = 100
strings_in_book = pages_in_book * 50
symbols_in_book = strings_in_book * 25
bytes_in_book = symbols_in_book * 4

disk_place_in_bytes = 1.44 * 1024 * 1024

num_of_books = disk_place_in_bytes // bytes_in_book

print("Количество книг, помещающихся на дискету:", int(num_of_books))