#!/bin/python

from PyQt5 import QtCore, QtGui, QtWidgets
from database import database

db = database("test")

# helper {{{

def qprint(msg):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog_Output(msg)
    dialog.ui.setupUi(dialog)
    dialog.exec_()

# }}}

# dialog view {{{
class Ui_Dialog_View(object):
    def __init__(self, key, value, name, search):
        self.name = name
        self.table = name.lower()
        self.key = key
        self.value = value
        self.search = search
    def setupUi(self, ViewUser):
        ViewUser.setObjectName("ViewUser")
        ViewUser.resize(704, 227)
        self.gridLayout = QtWidgets.QGridLayout(ViewUser)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(ViewUser)
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        key = self.key
        value = []
        search = self.search
        self.model.setHorizontalHeaderLabels(key)
        if search == 'id':
            value = self.value
            self.model.appendRow(value)
            self.model.setVerticalHeaderLabels([''])
        else:
            for i in range(0, len(self.value), 4):
                value.append(self.value[i:i+4])
            for i in value:
                if i != []:
                    print(i)
                    self.model.appendRow(i)
            self.model.setVerticalHeaderLabels([''] * len(value))

        self.retranslateUi(ViewUser)
        self.buttonBox.accepted.connect(ViewUser.accept) # type: ignore
        self.buttonBox.rejected.connect(ViewUser.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ViewUser)

    def retranslateUi(self, ViewUser):
        _translate = QtCore.QCoreApplication.translate
        ViewUser.setWindowTitle(_translate("ViewUser", f"{self.name} Details"))
# }}}

# main window {{{

# book view {{{
class Ui_Dialog_Main_View_Book(object):
    def __init__(self, name, cols):
        self.cols = cols
        self.name = name
    def setupUi(self, ViewUser):
        ViewUser.setObjectName("ViewBook")
        ViewUser.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout(ViewUser)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(ViewUser)
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        name = self.name.lower() 
        cols = self.cols
        # self.model.clear()
        self.model.setHorizontalHeaderLabels(cols)
        x = []
        tmp = db.table_sort(f"{name}", "*", "id")

        id_numbers = []
        for i in tmp:
            id_numbers.append(str(i[0]))

        x = []
        y = []
        for i in range(len(tmp)):
            for j in range(1, len(tmp[i])):
                x.append(QtGui.QStandardItem(tmp[i][j]))
            y.append(x)
            x = []

        for i in y:
            self.model.appendRow(i)

        self.model.setVerticalHeaderLabels(id_numbers)

        # key = self.key
        # value = self.value
        # self.model.setHorizontalHeaderLabels(key)
        # self.model.appendRow(value)
        # self.model.setVerticalHeaderLabels([''])

        self.retranslateUi(ViewUser)
        self.buttonBox.accepted.connect(ViewUser.accept) # type: ignore
        self.buttonBox.rejected.connect(ViewUser.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ViewUser)

    def retranslateUi(self, ViewUser):
        _translate = QtCore.QCoreApplication.translate
        ViewUser.setWindowTitle(_translate("ViewUser", f"{self.name} list"))
# }}}

# user view {{{
class Ui_Dialog_Main_View_User(object):
    def __init__(self, name, cols):
        self.cols = cols
        self.name = name
    def setupUi(self, ViewUser):
        ViewUser.setObjectName("ViewUser")
        ViewUser.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout(ViewUser)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(ViewUser)
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        name = self.name.lower() 
        cols = self.cols
        # self.model.clear()
        self.model.setHorizontalHeaderLabels(cols)
        x = []
        tmp = db.table_sort(f"{name}", "*", "id")

        id_numbers = []
        for i in tmp:
            id_numbers.append(str(i[0]))

        x = []
        y = []
        for i in range(len(tmp)):
            for j in range(1, len(tmp[i])):
                x.append(QtGui.QStandardItem(tmp[i][j]))
            y.append(x)
            x = []

        for i in y:
            self.model.appendRow(i)

        self.model.setVerticalHeaderLabels(id_numbers)

        # key = self.key
        # value = self.value
        # self.model.setHorizontalHeaderLabels(key)
        # self.model.appendRow(value)
        # self.model.setVerticalHeaderLabels([''])

        self.retranslateUi(ViewUser)
        self.buttonBox.accepted.connect(ViewUser.accept) # type: ignore
        self.buttonBox.rejected.connect(ViewUser.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ViewUser)

    def retranslateUi(self, ViewUser):
        _translate = QtCore.QCoreApplication.translate
        ViewUser.setWindowTitle(_translate("ViewUser", f"{self.name} list"))
# }}}

# stack view {{{
class Ui_Dialog_Main_View_Stack(object):
    def __init__(self, name, cols):
        self.cols = cols
        self.name = name
    def setupUi(self, ViewUser):
        ViewUser.setObjectName("ViewUser")
        ViewUser.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout(ViewUser)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(ViewUser)
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        name = self.name.lower() 
        cols = self.cols
        # self.model.clear()
        self.model.setHorizontalHeaderLabels(cols)
        x = []
        tmp = db.table_sort(f"{name}", "*", "id")

        id_numbers = []
        for i in tmp:
            id_numbers.append(str(i[0]))

        x = []
        y = []
        for i in range(len(tmp)):
            for j in range(1, len(tmp[i])):
                x.append(QtGui.QStandardItem(tmp[i][j]))
            y.append(x)
            x = []

        for i in y:
            self.model.appendRow(i)

        self.model.setVerticalHeaderLabels(id_numbers)

        # key = self.key
        # value = self.value
        # self.model.setHorizontalHeaderLabels(key)
        # self.model.appendRow(value)
        # self.model.setVerticalHeaderLabels([''])

        self.retranslateUi(ViewUser)
        self.buttonBox.accepted.connect(ViewUser.accept) # type: ignore
        self.buttonBox.rejected.connect(ViewUser.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ViewUser)

    def retranslateUi(self, ViewUser):
        _translate = QtCore.QCoreApplication.translate
        ViewUser.setWindowTitle(_translate("ViewUser", f"{self.name} list"))
# }}}

# }}}

# output {{{

# output new {{{

class Ui_Dialog_Output(object):
    def __init__(self, tmp):
        self.tmp = tmp
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 143)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">{self.tmp}</span></p></body></html>"))

# }}}

# # output box {{{
# class Ui_Dialog_Output_Box(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(346, 126)
#         self.gridLayout = QtWidgets.QGridLayout(Dialog)
#         self.gridLayout.setObjectName("gridLayout")
#         self.label = QtWidgets.QLabel(Dialog)
#         self.label.setObjectName("label")
#         self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setOrientation(QtCore.Qt.Vertical)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setCenterButtons(True)
#         self.buttonBox.setObjectName("buttonBox")
#         self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)
#         self.label_2 = QtWidgets.QLabel(Dialog)
#         self.label_2.setObjectName("label_2")
#         self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
#         self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">The book ID is [ ]</span></p></body></html>"))
#         self.label_2.setText(_translate("Dialog", "(?) You will need this ID later on"))
# # }}}

# }}}

# user {{{

# add user {{{
class Ui_Dialog_Add_User(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.the_title = QtWidgets.QLabel(Dialog)
        self.the_title.setObjectName("the_title")
        self.gridLayout.addWidget(self.the_title, 0, 0, 1, 2)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setObjectName("button_ok")
        self.gridLayout.addWidget(self.button_ok, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1, 0, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input_1 = QtWidgets.QLineEdit(Dialog)
        self.input_1.setInputMask("")
        self.input_1.setPlaceholderText("")
        self.input_1.setClearButtonEnabled(False)
        self.input_1.setObjectName("input_1")
        self.verticalLayout_4.addWidget(self.input_1)
        self.input_2 = QtWidgets.QLineEdit(Dialog)
        self.input_2.setInputMask("")
        self.input_2.setPlaceholderText("")
        self.input_2.setClearButtonEnabled(False)
        self.input_2.setObjectName("input_2")
        self.verticalLayout_4.addWidget(self.input_2)
        self.input_3 = QtWidgets.QLineEdit(Dialog)
        self.input_3.setInputMask("")
        self.input_3.setPlaceholderText("")
        self.input_3.setClearButtonEnabled(False)
        self.input_3.setObjectName("input_3")
        self.verticalLayout_4.addWidget(self.input_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 3, 0, 1, 1)
        self.the_error = QtWidgets.QLabel(Dialog)
        self.the_error.setObjectName("the_error")
        self.gridLayout.addWidget(self.the_error, 1, 0, 1, 2)
        # buttons {{{
        self.button_cancel.clicked.connect(self.exit_button_clicked)
        self.button_ok.clicked.connect(self.ok_button_clicked)
        # }}}
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_button_clicked(self):
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            err = db.table_insert("users", "(username, address, phone)", tuple(x))
            if err == 0:
                qprint(f"something is wrong with {x}")
            else:
                qprint(f"User added: {x}")
                self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add user"))
        self.the_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Add user to the database</span></p></body></html>"))
        self.button_ok.setText(_translate("Dialog", "OK"))
        self.label_1.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Address"))
        self.label_3.setText(_translate("Dialog", "Phone NO."))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))
        self.the_error.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
# }}}

# search user {{{
class Ui_Dialog_Search_User(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 275)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Group for the first set of radio buttons
        self.buttonGroup1 = QtWidgets.QButtonGroup(Dialog)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_3)

        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_4)

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 2)
        self.buttonGroup1.addButton(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_2)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        # Group for the second set of radio buttons
        self.buttonGroup2 = QtWidgets.QButtonGroup(Dialog)

        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 5, 0, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_5)

        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 5, 1, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_6)

        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 5, 2, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_7)

        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 6, 0, 1, 1)
        self.pushButton_OK.clicked.connect(self.ok_button_clicked)

        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 6, 2, 1, 1)
        self.pushButton_Cancel.clicked.connect(self.exit_button_clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_button_clicked(self):
        # print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        self.name = "Users"
        self.table = self.name.lower()
        table = self.table

        self.tmp = self.lineEdit.text()
        tmp = self.tmp

        search_by = []
        operation = []

        if tmp != '' and tmp != None:
            for button in self.buttonGroup1.buttons():
                if button.isChecked():
                    search_by.append(button.text())

            for button in self.buttonGroup2.buttons():
                if button.isChecked():
                    operation.append(button.text())

            self.search_user = ""
            match search_by[0]:
                case "User ID":
                    self.search_user = "id"
                case "User Name":
                    self.search_user = "username"
                case "Address":
                    self.search_user = "address"
                case "Phone NO.":
                    self.search_user = "phone"

            search = self.search_user

            match operation[0]:
                case "View":
                    err = db.table_filter(table, "*", search, tmp)
                    if err == []:
                        qprint(f"User with {search} = {tmp} is invalid")
                    else:
                        key = ["ID", "User Name", "Address", "Phone NO."]
                        value = []
                        for i in err:
                            for j in i:
                                value.append(QtGui.QStandardItem(str(j)))

                        dialog = QtWidgets.QDialog()
                        dialog.ui = Ui_Dialog_View(key, value, self.name, search)
                        dialog.ui.setupUi(dialog)
                        dialog.exec_()
                            
                case "Edit":
                    err = db.table_filter(table, "*", search, tmp)
                    if err == []:
                        qprint(f"User with {search} = {tmp} is invalid")
                    else:
                        key = ["User Name", "Address", "Phone NO."]
                        value = []
                        for i in err:
                            for j in i:
                                value.append(QtGui.QStandardItem(str(j)))

                        dialog = QtWidgets.QDialog()
                        dialog.ui = Ui_Dialog_Edit_User(key, value, table, search, tmp)
                        dialog.ui.setupUi(dialog)
                        dialog.exec_()

                case "Delete":
                    err = db.table_delete(table, search, tmp)
                    if err == 0:
                        qprint(f"User with {search} = {tmp} is invalid")
                    else:
                        qprint(f"User deleted")

            self.Dialog.close()
        else:
            qprint("You need to enter a value")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search users"))
        self.label.setText(_translate("Dialog", "Search user by:"))
        self.radioButton_3.setText(_translate("Dialog", "User ID"))
        self.radioButton_4.setText(_translate("Dialog", "Publisher"))
        self.radioButton.setText(_translate("Dialog", "User Name"))
        self.radioButton_2.setText(_translate("Dialog", "Author Name"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Operation</span></p></body></html>"))
        self.radioButton_5.setText(_translate("Dialog", "Delete"))
        self.radioButton_6.setText(_translate("Dialog", "View"))
        self.radioButton_7.setText(_translate("Dialog", "Edit"))

        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
# }}}

# # user view {{{
# class Ui_Dialog_View_User(object):
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#     def setupUi(self, ViewUser):
#         ViewUser.setObjectName("ViewUser")
#         ViewUser.resize(704, 227)
#         self.gridLayout = QtWidgets.QGridLayout(ViewUser)
#         self.gridLayout.setObjectName("gridLayout")
#         self.tableView = QtWidgets.QTableView(ViewUser)
#         self.tableView.setObjectName("tableView")
#         self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
#         self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
#         self.tableView.setModel(self.model)
#         self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
#         self.buttonBox = QtWidgets.QDialogButtonBox(ViewUser)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
#
#         key = self.key
#         value = self.value
#         self.model.setHorizontalHeaderLabels(key)
#         self.model.appendRow(value)
#         self.model.setVerticalHeaderLabels([''])
#
#         self.retranslateUi(ViewUser)
#         self.buttonBox.accepted.connect(ViewUser.accept) # type: ignore
#         self.buttonBox.rejected.connect(ViewUser.reject) # type: ignore
#         QtCore.QMetaObject.connectSlotsByName(ViewUser)
#
#     def retranslateUi(self, ViewUser):
#         _translate = QtCore.QCoreApplication.translate
#         ViewUser.setWindowTitle(_translate("ViewUser", "User Details"))
# # }}}

# user edit {{{
class Ui_Dialog_Edit_User(object):
    def __init__(self, key, value, table, search, tmp):
        self.key = key
        self.value = value
        self.table = table
        self.search = search
        self.tmp = tmp
    def setupUi(self, ViewUser):
        self.ViewUser = ViewUser
        ViewUser.setObjectName("ViewUser")
        ViewUser.resize(704, 227)
        self.gridLayout = QtWidgets.QGridLayout(ViewUser)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_cancel = QtWidgets.QPushButton(ViewUser)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(ViewUser)
        self.tableView.setObjectName("tableView")

        # self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 2)
        self.pushButton_save = QtWidgets.QPushButton(ViewUser)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 1)

        key = self.key
        value = self.value
        self.id_number = value[0].text()
        self.model.setHorizontalHeaderLabels(key[1:])
        self.model.appendRow(value[1:])
        self.model.setVerticalHeaderLabels([self.id_number])

        self.pushButton_save.clicked.connect(self.button_save_clicked)
        self.pushButton_cancel.clicked.connect(self.button_cancel_clicked)

        self.retranslateUi(ViewUser)
        QtCore.QMetaObject.connectSlotsByName(ViewUser)

    def retranslateUi(self, ViewUser):
        _translate = QtCore.QCoreApplication.translate
        ViewUser.setWindowTitle(_translate("ViewUser", "User Details"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))

    def button_save_clicked(self):
        table = self.table # users
        search = self.search # idk yet
        tmp = self.tmp # prompt

        updated_data = []
        for row in range(self.model.rowCount()):
            row_data = []
            for column in range(self.model.columnCount()):
                item = self.model.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    qprint(f"item ({row},{column}) cannot be empty")
                    # row_data.append("")  # Handle the case when the item is None
            updated_data.append(row_data)

        # Print the updated data
        # print("Updated Data:")
        # data = []
        # for row in updated_data:
        #     data.append(row)

        sql_data = f"username = '{updated_data[0][0]}', address = '{updated_data[0][1]}', phone = '{updated_data[0][2]}'"
        qprint(str(sql_data))
        err = db.table_update(table, f"{search} = {tmp}", sql_data)
        if err == 0:
            qprint(f"User with {search} = {tmp} is invalid")
        else:
            qprint(f"User updated")
        self.ViewUser.close()

    def button_cancel_clicked(self):
        self.ViewUser.close()
# }}}

# }}}

# book {{{

# add book {{{
class Ui_Dialog_Add_Book(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.the_title = QtWidgets.QLabel(Dialog)
        self.the_title.setObjectName("the_title")
        self.gridLayout.addWidget(self.the_title, 0, 0, 1, 2)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setObjectName("button_ok")
        self.gridLayout.addWidget(self.button_ok, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1, 0, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input_1 = QtWidgets.QLineEdit(Dialog)
        self.input_1.setInputMask("")
        self.input_1.setPlaceholderText("")
        self.input_1.setClearButtonEnabled(False)
        self.input_1.setObjectName("input_1")
        self.verticalLayout_4.addWidget(self.input_1)
        self.input_2 = QtWidgets.QLineEdit(Dialog)
        self.input_2.setInputMask("")
        self.input_2.setPlaceholderText("")
        self.input_2.setClearButtonEnabled(False)
        self.input_2.setObjectName("input_2")
        self.verticalLayout_4.addWidget(self.input_2)
        self.input_3 = QtWidgets.QLineEdit(Dialog)
        self.input_3.setInputMask("")
        self.input_3.setPlaceholderText("")
        self.input_3.setClearButtonEnabled(False)
        self.input_3.setObjectName("input_3")
        self.verticalLayout_4.addWidget(self.input_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 3, 0, 1, 1)
        self.the_error = QtWidgets.QLabel(Dialog)
        self.the_error.setObjectName("the_error")
        self.gridLayout.addWidget(self.the_error, 1, 0, 1, 2)
        # buttons {{{
        self.button_cancel.clicked.connect(self.exit_button_clicked)
        self.button_ok.clicked.connect(self.ok_button_clicked)
        # }}}
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_button_clicked(self):
        # print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            err = db.table_insert("books", "(book, author, publisher)", tuple(x))
            if err == 0:
                qprint(f"something is wrong with {x}")
            else:
                qprint(f"Book added: {x}")
                self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add book"))
        self.the_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Add Book to the library</span></p></body></html>"))
        self.button_ok.setText(_translate("Dialog", "OK"))
        self.label_1.setText(_translate("Dialog", "Book Name"))
        self.label_2.setText(_translate("Dialog", "Author"))
        self.label_3.setText(_translate("Dialog", "Publisher"))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))
        self.the_error.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
# }}}

# search book {{{
class Ui_Dialog_Search_Book(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 275)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Group for the first set of radio buttons
        self.buttonGroup1 = QtWidgets.QButtonGroup(Dialog)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_3)

        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_4)

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 2)
        self.buttonGroup1.addButton(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_2)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        # Group for the second set of radio buttons
        self.buttonGroup2 = QtWidgets.QButtonGroup(Dialog)

        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 5, 0, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_5)

        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 5, 1, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_6)

        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 5, 2, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_7)

        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 6, 0, 1, 1)
        self.pushButton_OK.clicked.connect(self.ok_button_clicked)

        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 6, 2, 1, 1)
        self.pushButton_Cancel.clicked.connect(self.exit_button_clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_button_clicked(self):
        # print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        self.name = "Books"
        self.table = self.name.lower()
        table = self.table

        self.tmp = self.lineEdit.text()
        tmp = self.tmp

        search_by = []
        operation = []

        if tmp != '' and tmp != None:
            for button in self.buttonGroup1.buttons():
                if button.isChecked():
                    search_by.append(button.text())

            for button in self.buttonGroup2.buttons():
                if button.isChecked():
                    operation.append(button.text())

            self.search_book = ""
            match search_by[0]:
                case "Book ID":
                    self.search_book = "id"
                case "Book Name":
                    self.search_book = "book"
                case "Publisher":
                    self.search_book = "publisher"
                case "Author Name":
                    self.search_book = "author"

            search = self.search_book

            match operation[0]:
                case "View":
                    err = db.table_filter(table, "*", search, tmp)
                    if err == []:
                        qprint(f"Book with {search} = {tmp} is invalid")
                    else:
                        key = ["ID", "Book Name", "Author", "Publisher"]
                        value = []
                        for i in err:
                            for j in i:
                                value.append(QtGui.QStandardItem(str(j)))

                        dialog = QtWidgets.QDialog()
                        dialog.ui = Ui_Dialog_View(key, value, self.name, search)
                        dialog.ui.setupUi(dialog)
                        dialog.exec_()
                            
                case "Edit":
                    err = db.table_filter(table, "*", search, tmp)
                    if err == []:
                        qprint(f"Book with {search} = {tmp} is invalid")
                    else:
                        key = ["ID", "Book Name", "Author", "Publisher"]
                        value = []
                        for i in err:
                            for j in i:
                                value.append(QtGui.QStandardItem(str(j)))

                        dialog = QtWidgets.QDialog()
                        dialog.ui = Ui_Dialog_Edit_Book(key, value, table, search, tmp)
                        dialog.ui.setupUi(dialog)
                        dialog.exec_()

                case "Delete":
                    err = db.table_delete(table, search, tmp)
                    if err == 0:
                        qprint(f"Book with {search} = {tmp} is invalid")
                    else:
                        qprint(f"Book deleted")

            self.Dialog.close()
        else:
            qprint("You need to enter a value")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search books"))
        self.label.setText(_translate("Dialog", "Search book by:"))
        self.radioButton_3.setText(_translate("Dialog", "Book ID"))
        self.radioButton_4.setText(_translate("Dialog", "Publisher"))
        self.radioButton.setText(_translate("Dialog", "Book Name"))
        self.radioButton_2.setText(_translate("Dialog", "Author Name"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Operation</span></p></body></html>"))
        self.radioButton_5.setText(_translate("Dialog", "Delete"))
        self.radioButton_6.setText(_translate("Dialog", "View"))
        self.radioButton_7.setText(_translate("Dialog", "Edit"))

        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
# }}}

# # book view {{{
# class Ui_Dialog_View_Book(object):
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#     def setupUi(self, ViewBook):
#         ViewBook.setObjectName("ViewBook")
#         ViewBook.resize(704, 227)
#         self.gridLayout = QtWidgets.QGridLayout(ViewBook)
#         self.gridLayout.setObjectName("gridLayout")
#         self.tableView = QtWidgets.QTableView(ViewBook)
#         self.tableView.setObjectName("tableView")
#         self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
#         self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
#         self.tableView.setModel(self.model)
#         self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
#         self.buttonBox = QtWidgets.QDialogButtonBox(ViewBook)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
#
#         key = self.key
#         value = self.value
#         self.model.setHorizontalHeaderLabels(key)
#         self.model.appendRow(value)
#         self.model.setVerticalHeaderLabels([''])
#
#         self.retranslateUi(ViewBook)
#         self.buttonBox.accepted.connect(ViewBook.accept) # type: ignore
#         self.buttonBox.rejected.connect(ViewBook.reject) # type: ignore
#         QtCore.QMetaObject.connectSlotsByName(ViewBook)
#
#     def retranslateUi(self, ViewBook):
#         _translate = QtCore.QCoreApplication.translate
#         ViewBook.setWindowTitle(_translate("ViewBook", "Book Details"))
# # }}}

# book edit {{{
class Ui_Dialog_Edit_Book(object):
    def __init__(self, key, value, table, search, tmp):
        self.key = key
        self.value = value
        self.table = table
        self.search = search
        self.tmp = tmp
    def setupUi(self, ViewBook):
        self.ViewBook = ViewBook
        ViewBook.setObjectName("ViewBook")
        ViewBook.resize(704, 227)
        self.gridLayout = QtWidgets.QGridLayout(ViewBook)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_cancel = QtWidgets.QPushButton(ViewBook)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(ViewBook)
        self.tableView.setObjectName("tableView")

        # self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 2)
        self.pushButton_save = QtWidgets.QPushButton(ViewBook)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 1)

        key = self.key
        value = self.value
        self.id_number = value[0].text()
        self.model.setHorizontalHeaderLabels(key[1:])
        self.model.appendRow(value[1:])
        self.model.setVerticalHeaderLabels([self.id_number])

        self.pushButton_save.clicked.connect(self.button_save_clicked)
        self.pushButton_cancel.clicked.connect(self.button_cancel_clicked)

        self.retranslateUi(ViewBook)
        QtCore.QMetaObject.connectSlotsByName(ViewBook)

    def retranslateUi(self, ViewBook):
        _translate = QtCore.QCoreApplication.translate
        ViewBook.setWindowTitle(_translate("ViewBook", "Book Details"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))

    def button_save_clicked(self):
        table = self.table # books
        search = self.search # idk yet
        tmp = self.tmp # prompt

        updated_data = []
        for row in range(self.model.rowCount()):
            row_data = []
            for column in range(self.model.columnCount()):
                item = self.model.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    qprint(f"item ({row},{column}) cannot be empty")
                    # row_data.append("")  # Handle the case when the item is None
            updated_data.append(row_data)

        sql_data = f"book = '{updated_data[0][0]}', author = '{updated_data[0][1]}', publisher = '{updated_data[0][2]}'"
        qprint(str(sql_data))
        err = db.table_update(table, f"{search} = {tmp}", sql_data)
        if err == 0:
            qprint(f"Book with {search} = {tmp} is invalid")
        else:
            qprint(f"Book updated")
        self.ViewBook.close()

    def button_cancel_clicked(self):
        self.ViewBook.close()
# }}}

# }}}

# stack {{{

# search stack {{{
class Ui_Dialog_Search_Stack(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 275)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Group for the first set of radio buttons
        self.buttonGroup1 = QtWidgets.QButtonGroup(Dialog)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_3)

        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_4)

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 2)
        self.buttonGroup1.addButton(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_2)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        # Group for the second set of radio buttons
        self.buttonGroup2 = QtWidgets.QButtonGroup(Dialog)

        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 5, 0, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_5)

        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 5, 1, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_6)

        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 5, 2, 1, 1)
        self.buttonGroup2.addButton(self.radioButton_7)

        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 6, 0, 1, 1)
        self.pushButton_OK.clicked.connect(self.ok_button_clicked)

        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 6, 2, 1, 1)
        self.pushButton_Cancel.clicked.connect(self.exit_button_clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_button_clicked(self):
        self.Dialog.close()

    def ok_button_clicked(self):
        self.name = "Stack"
        self.table = self.name.lower()
        table = self.table

        self.tmp = self.lineEdit.text()
        tmp = self.tmp

        search_by = []
        operation = []

        if tmp != '' and tmp != None:
            for button in self.buttonGroup1.buttons():
                if button.isChecked():
                    search_by.append(button.text())

            for button in self.buttonGroup2.buttons():
                if button.isChecked():
                    operation.append(button.text())

            self.search_book = ""
            match search_by[0]:
                case "Stack ID":
                    self.search_book = "id"
                case "Book ID":
                    self.search_book = "book_id"
                case "User ID":
                    self.search_book = "user_id"
                case "Date":
                    self.search_book = "date"

            search = self.search_book

            print(f"{table} {search} {tmp}")

            match operation[0]:
                case "View":
                    err = db.table_filter(table, "*", search, tmp)
                    if err == []:
                        qprint(f"Stack with {search} = {tmp} is invalid")
                    else:
                        key = ["ID", "User ID", "Book ID", "Date"]
                        value = []
                        for i in err:
                            for j in i:
                                value.append(QtGui.QStandardItem(str(j)))

                        dialog = QtWidgets.QDialog()
                        dialog.ui = Ui_Dialog_View(key, value, self.name, search)
                        dialog.ui.setupUi(dialog)
                        dialog.exec_()
                            
                case "Edit":
                    err = db.table_filter(table, "*", search, tmp)
                    if err == []:
                        qprint(f"Stack with {search} = {tmp} is invalid")
                    else:
                        key = ["ID", "User ID", "Book ID", "Date"]
                        value = []
                        for i in err:
                            for j in i:
                                value.append(QtGui.QStandardItem(str(j)))

                        dialog = QtWidgets.QDialog()
                        dialog.ui = Ui_Dialog_Edit_Stack(key, value, table, search, tmp)
                        dialog.ui.setupUi(dialog)
                        dialog.exec_()

                case "Delete":
                    err = db.table_delete(table, search, tmp)
                    if err == 0:
                        qprint(f"Stack with {search} = {tmp} is invalid")
                    else:
                        qprint(f"Stack deleted")

            self.Dialog.close()
        else:
            qprint("You need to enter a value")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search stack"))
        self.label.setText(_translate("Dialog", "Search stack by:"))
        self.radioButton_3.setText(_translate("Dialog", "Stack ID"))
        self.radioButton_4.setText(_translate("Dialog", "Date"))
        self.radioButton.setText(_translate("Dialog", "User ID"))
        self.radioButton_2.setText(_translate("Dialog", "Book ID"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Operation</span></p></body></html>"))
        self.radioButton_5.setText(_translate("Dialog", "Delete"))
        self.radioButton_6.setText(_translate("Dialog", "View"))
        self.radioButton_7.setText(_translate("Dialog", "Edit"))

        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
# }}}

# add stack {{{

class Ui_Dialog_Add_Stack(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.the_title = QtWidgets.QLabel(Dialog)
        self.the_title.setObjectName("the_title")
        self.gridLayout.addWidget(self.the_title, 0, 0, 1, 2)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setObjectName("button_ok")
        self.gridLayout.addWidget(self.button_ok, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1, 0, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input_1 = QtWidgets.QLineEdit(Dialog)
        self.input_1.setInputMask("")
        self.input_1.setPlaceholderText("")
        self.input_1.setClearButtonEnabled(False)
        self.input_1.setObjectName("input_1")
        self.verticalLayout_4.addWidget(self.input_1)
        self.input_2 = QtWidgets.QLineEdit(Dialog)
        self.input_2.setInputMask("")
        self.input_2.setPlaceholderText("")
        self.input_2.setClearButtonEnabled(False)
        self.input_2.setObjectName("input_2")
        self.verticalLayout_4.addWidget(self.input_2)
        self.input_3 = QtWidgets.QLineEdit(Dialog)
        self.input_3.setInputMask("")
        self.input_3.setPlaceholderText("2020/12/1")
        self.input_3.setClearButtonEnabled(False)
        self.input_3.setObjectName("input_3")
        self.verticalLayout_4.addWidget(self.input_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 3, 0, 1, 1)
        self.the_error = QtWidgets.QLabel(Dialog)
        self.the_error.setObjectName("the_error")
        self.gridLayout.addWidget(self.the_error, 1, 0, 1, 2)
        # buttons {{{
        self.button_cancel.clicked.connect(self.exit_button_clicked)
        self.button_ok.clicked.connect(self.ok_button_clicked)
        # }}}
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_button_clicked(self):
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            err = db.table_insert("stack", "(user_id, book_id, date)", tuple(x))
            # err = 1
            if err == 0:
                qprint(f"something is wrong with {x}")
            else:
                qprint(f"Book {x[0]} has lended to user {x[1]} at {x[2]}")
                self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lend Book"))
        self.the_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Lend a book to a user</span></p></body></html>"))
        self.button_ok.setText(_translate("Dialog", "OK"))
        self.label_1.setText(_translate("Dialog", "Book ID"))
        self.label_2.setText(_translate("Dialog", "User ID"))
        self.label_3.setText(_translate("Dialog", "Date of lend"))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))
        self.the_error.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

# }}}

# stack edit {{{
class Ui_Dialog_Edit_Stack(object):
    def __init__(self, key, value, table, search, tmp):
        self.key = key
        self.value = value
        self.table = table
        self.search = search
        self.tmp = tmp
    def setupUi(self, ViewBook):
        self.ViewBook = ViewBook
        ViewBook.setObjectName("ViewBook")
        ViewBook.resize(704, 227)
        self.gridLayout = QtWidgets.QGridLayout(ViewBook)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_cancel = QtWidgets.QPushButton(ViewBook)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(ViewBook)
        self.tableView.setObjectName("tableView")

        # self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 2)
        self.pushButton_save = QtWidgets.QPushButton(ViewBook)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 1)

        key = self.key
        value = self.value
        self.id_number = value[0].text()
        self.model.setHorizontalHeaderLabels(key[1:])
        self.model.appendRow(value[1:])
        self.model.setVerticalHeaderLabels([self.id_number])

        self.pushButton_save.clicked.connect(self.button_save_clicked)
        self.pushButton_cancel.clicked.connect(self.button_cancel_clicked)

        self.retranslateUi(ViewBook)
        QtCore.QMetaObject.connectSlotsByName(ViewBook)

    def retranslateUi(self, ViewBook):
        _translate = QtCore.QCoreApplication.translate
        ViewBook.setWindowTitle(_translate("ViewBook", "Stack Details"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))

    def button_save_clicked(self):
        table = self.table # stack
        search = self.search # search filter
        tmp = self.tmp # prompt

        updated_data = []
        for row in range(self.model.rowCount()):
            row_data = []
            for column in range(self.model.columnCount()):
                item = self.model.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    qprint(f"item ({row},{column}) cannot be empty")
                    # row_data.append("")  # Handle the case when the item is None
            updated_data.append(row_data)

        sql_data = f"user_id = '{updated_data[0][0]}', book_id = '{updated_data[0][1]}', date = '{updated_data[0][2]}'"
        qprint(str(sql_data))
        err = db.table_update(table, f"{search} = {tmp}", sql_data)
        if err == 0:
            qprint(f"Stack with {search} = {tmp} is invalid")
        else:
            qprint(f"Stack updated")
        self.ViewBook.close()

    def button_cancel_clicked(self):
        self.ViewBook.close()
# }}}

# }}}

