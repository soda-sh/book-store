# book-store

Simple QT application to manage a small book library
with database.

## Structure

We are going to need 4 classes with the following methods:

+ `User` -- Manage (Create, Delete, Update) users
    + `UserAdd()`
    + `UserDelete()`
    + `UserEdit`
    + `UserShow()`
+ `Book` -- Same as the `User` class but for the books
    + `BookAdd()`
    + `BookDelete()`
    + `BookEdit`
    + `BookShow()`
+ `Order` -- Manage assigning/resigning a book to/from a user
    + `OrderAdd()`
    + `OrderDelete()`
    + `OrderEdit`
    + `OrderShow()`
+ `Stock` -- The status of in-use books and users' book status
    + `StockAdd()`
    + `StockDelete()`
    + `StockEdit`
    + `StockShow()`

## Setup Dev Environment

I suggest to use venv:

    python -m venv env_name

And then install the qt and other stuff

### Activate venv

    source env_name/bin/activate

After activating, you should see the name of environment before your shell's
prompt:

    (env_name) [user@hostname]$

### pyqt5

    pip install pyqt5
