size_mb = 1.44   # TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
symbols_bytes = 4

size_bytes = size_mb * 1024 * 1024
symbols_book = pages * lines * symbols
size_book_bytes = symbols_book * symbols_bytes
book_count = int(size_bytes // size_book_bytes)

print("Количество книг, помещающихся на дискету:", book_count)
