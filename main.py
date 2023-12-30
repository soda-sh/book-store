#!/usr/bin/env python3

from Book import Book as b

book_1 = b({
    "name": "Hos",
    "password": "xyz",
    "id": "123",
})

temp = book_1.Show_Column()

for key in temp:
    print(key, temp[key])

print("-"*10)
print(book_1.Add_Column("Add_Column"))

print("-"*10)
print(book_1.Rem_Column("Rem_Column"))
