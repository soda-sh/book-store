#!/bin/python

import mysql.connector as mc
# from random import randrange as rr

class database():
    # init {{{
    def __init__(self, name):
        self.database_name = name
        self.user = "book"
        self.password = "book"
        self.host = "localhost"
        self.db = mc.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database_name,
        )
        self.cursor = self.db.cursor()
    # }}}

    # helper functions {{{
    def check_exists(self, name, kind):
        not_exists = True
        for i in kind:
            for j in i:
                if j != name and not_exists == True:
                    not_exists = False
        return not_exists
    # }}}

    # create database {{{
    def database_create(self):
        tmp = ""
        name = self.database_name
        self.cursor.execute("SHOW DATABASES")
        if not self.check_exists(name, self.cursor): # create database if does not exists
            self.cursor.execute(f"CREATE DATABASE {name}")
            tmp = f"database created: {name}"
        else:
            tmp = f"database exists: {name}"
        return tmp
    # }}}

    # tables {{{

    # create table {{{
    def table_create(self, name, rows):
        tmp = ""
        self.cursor.execute("SHOW TABLES")
        not_exists = True
        for i in self.cursor:
            for j in i:
                if j != name:
                    not_exists = False
        if not_exists: # create table if does not exists
            sql = f"CREATE TABLE {name} (id INT AUTO_INCREMENT PRIMARY KEY, {rows})"
            self.cursor.execute(sql)
            tmp = f"table created: {name}"
        else:
            tmp = f"table exists: {name}"
        return tmp
    # }}}

    # insert into table {{{
    def table_insert(self, name, key, value):
        sql = f"INSERT INTO {name} {key} VALUES (%s, %s, %s)"
        self.cursor.execute(sql, value)

        self.db.commit() # this is required to make the changes, otherwise no changes are made to the table
        tmp = self.cursor.rowcount
        return tmp
    # }}}

    # select table {{{
    def table_select(self, name, key):
        self.cursor.execute(f"SELECT {key} FROM {name}")
        tmp = self.cursor.fetchone()
        return tmp
    # }}}

    # filter table {{{
    def table_filter(self, name, what, key, value):
        sql = f"SELECT {what} FROM {name} WHERE {key} = {value}"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        return tmp

    # }}}

    # order table {{{
    def table_sort(self, name, key, value):
        sql = f"SELECT {key} FROM {name} ORDER BY {value}"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        return tmp
    # }}}

    # delete table {{{
    def table_delete(self, name, key, value):
        sql = f"DELETE FROM {name} WHERE {key} = {value}"
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.rowcount

    # }}}

    # drop table {{{
    def table_drop(self, name):
        sql = f"DROP TABLE IF EXISTS {name}"
        self.cursor.execute(sql)
        # tmp = f"table {name} dropped"
        # return tmp
    # }}}

    # update table {{{
    def table_update(self, name, old, new):
        sql = f"UPDATE {name} SET {new} WHERE {old}"
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.rowcount
    # }}}
    
    # }}}

database_name = "test"
tmp = database(database_name)

tmp.table_create("users", "username VARCHAR(255), address VARCHAR(255), phone VARCHAR(255)")
tmp.table_create("books", "book VARCHAR(255), author VARCHAR(255), publisher VARCHAR(255)")
tmp.table_create("stack", "user_id VARCHAR(255), book_id VARCHAR(255), date VARCHAR(255)")

# # tests {{{

# # insert dump data
# dmp_users = [
#     ["Hos", "localhost", "1327"],
#     ["Zapp", "SAW", "1234"],
# ]
# for i in dmp_users:
#     test = tmp.table_insert("users", "(username, address, phone)", tuple(i))
#     print(tuple(i))
# ###
# dmp_books = [
#     ["The C Programming", "K&R", "idk"],
#     ["How to Become a Hacker", "Erick Raymond", "idk"],
# ]
# for i in dmp_books:
#     test = tmp.table_insert("books", "(book, author, publisher)", tuple(i))
#     print(tuple(i))
# ###
# dmp_stack = [
#     ["1", "2", "2023/12/28"],
#     ["2", "1", "2023/10/18"],
# ]
# for i in dmp_stack:
#     test = tmp.table_insert("stack", "(user_id, book_id, date)", tuple(i))
#     print(tuple(i))

# test = []

# test = tmp.table_select("users", "username")
# test = tmp.table_filter("books", "*", "book", "'Simple book'")
# test = tmp.table_insert("customers", "(name, address)", ("John", "Highway 21"))
# test = tmp.table_delete("customers", "*", "52")
# test = tmp.table_delete("customers", "id", "51")
# test = tmp.table_sort("books", "*", "id") # apend ` DESC` to reversed sort
# test = tmp.table_update("books", "id = 1", "book = 'Simple book', author = 'Who Knows', publisher = 'TodayLand'")

# test = tmp.table_filter("stack", "*", "id", "1")
# for key in test:
#     print(key)

# # }}}

