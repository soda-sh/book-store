#!/bin/python

import mysql.connector as mc
# from random import randrange as rr

class database():
    # init {{{
    def __init__(self):
        self.database_name = "test"
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
        exists = False
        for key in kind:
            if key[0] == name and exists == False:
                return True
        return False
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
    def table_create(self, name):
        tmp = ""
        self.cursor.execute("SHOW TABLES")
        if not self.check_exists(name, self.cursor): # create table if does not exists
            sql = f"CREATE TABLE {name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
            self.cursor.execute(sql)
            tmp = f"table created: {name}"
        else:
            tmp = f"table exists: {name}"
        return tmp
    # }}}

    # insert into table {{{
    def table_insert(self, name, key, value):
        sql = f"INSERT INTO {name} {key} VALUES (%s, %s)"
        self.cursor.execute(sql, value)

        self.db.commit() # this is required to make the changes, otherwise no changes are made to the table
        tmp = self.cursor.rowcount, "was inserted."
        print("1 record inserted, ID:", self.cursor.lastrowid)
        return tmp
    # }}}

    # select table {{{
    def table_select(self, name, key):
        self.cursor.execute(f"SELECT {key} FROM {name}")
        tmp = self.cursor.fetchone()
        return tmp
        # print(tmp)
        # for key in tmp:
        #     print(key)
    # }}}

    # filter table {{{
    def table_filter(self, name, what, key, value):
        sql = f"SELECT {what} FROM {name} WHERE {key} = {value}"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        return tmp
        # print(tmp)
        # for key in tmp:
        #     print(key)

    # }}}

    # order table {{{
    def table_sort(self, name, key, value):
        sql = f"SELECT {key} FROM {name} ORDER BY {value}"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        return tmp
        # print(tmp)
        # for key in tmp:
        #     print('\t', key)
    # }}}

    # delete table {{{
    def table_delete(self, name, key, value):
        sql = f"DELETE FROM {name} WHERE {key} = {value}"
        self.cursor.execute(sql)
        self.db.commit()
        tmp = f"{self.cursor.rowcount} record(s) deleted"
        return tmp

    # }}}

    # drop table {{{
    def table_drop(self, name):
        sql = "DROP TABLE IF EXISTS {name}"
        self.cursor.execute(sql)
        tmp = f"table {name} dropped"
        return tmp
    # }}}

    # update table {{{
    def table_update(self, name, old, new):
        sql = f"UPDATE {name} SET {new} WHERE {old}"
        self.cursor.execute(sql)
        self.db.commit()
        tmp = f"{self.cursor.rowcount} record(s) affected"
        return tmp
    # }}}
    
    # }}}


# val = [('Peter', 'Lowstreet 4'), ('Peter', 'Lowstreet 4')]
# val = ('Peter', 'Lowstreet 4'),

tmp = database()
# test = tmp.database_create()
# test = tmp.table_create("customers")
# test = tmp.table_select("customers", "id")
# test = tmp.table_filter("customers", "*", "address", "'Park Lane 38'")
# test = tmp.table_insert("customers", "(name, address)", ("John", "Highway 21"))
# test = tmp.table_delete("customers", "*", "52")
test = tmp.table_sort("customers", "*", "id") # apend ` DESC` to reversed sort
# test = tmp.table_delete("customers", "id", "51")
# test = tmp.table_update("customers", "name = 'Amy'", "name = 'Hos'")

for key in test:
    print(key)

