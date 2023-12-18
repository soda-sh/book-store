#!/usr/bin/env python3

from Book import Book as b

book_1 = b("Hos", "xyz", "123")

temp = book_1.Show_Column()

for key in temp:
    print(key, temp[key])
