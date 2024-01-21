#!/bin/python

from PyQt5 import QtCore, QtGui, QtWidgets

# helper {{{

def qprint(msg):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog_Output(msg)
    dialog.ui.setupUi(dialog)
    dialog.exec_()

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
        print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        print("OK button clicked")
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            print(tuple(x))
            for i in range(len(x)):
                print(x[i])
            qprint("User added")
            self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.the_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Add user to the database</span></p></body></html>"))
        self.button_ok.setText(_translate("Dialog", "OK"))
        self.label_1.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Address"))
        self.label_3.setText(_translate("Dialog", "Phone NO."))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))
        self.the_error.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
# }}}

# edit user {{{
class Ui_Dialog_Edit_User(object):
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
        print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        print("OK button clicked")
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            print(tuple(x))
            for i in range(len(x)):
                print(x[i])
            qprint("User updated")
            self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit User"))
        self.the_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Edit a user's informations</span></p></body></html>"))
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
        print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        tmp = self.lineEdit.text()
        if tmp != '' and tmp != None:
            print(tmp)
        for button in self.buttonGroup1.buttons():
            if button.isChecked():
                print(button.text() + " is checked")

        for button in self.buttonGroup2.buttons():
            if button.isChecked():
                print(button.text() + " is checked")
        self.Dialog.close()

    # def check_buttons(self):
    #     for button in self.buttonGroup1.buttons():
    #         if button.isChecked():
    #             print(button.text() + " is checked")
    #
    #     for button in self.buttonGroup2.buttons():
    #         if button.isChecked():
    #             print(button.text() + " is checked")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Search book by:</span></p></body></html>"))
        self.radioButton_3.setText(_translate("Dialog", "User ID"))
        self.radioButton_4.setText(_translate("Dialog", "User Name"))
        self.radioButton.setText(_translate("Dialog", "Address"))
        self.radioButton_2.setText(_translate("Dialog", "Phone NO."))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Operation</span></p></body></html>"))
        self.radioButton_5.setText(_translate("Dialog", "Delete"))
        self.radioButton_6.setText(_translate("Dialog", "View"))
        self.radioButton_7.setText(_translate("Dialog", "Edit"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
# }}}

# delete user {{{

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
        print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        print("OK button clicked")
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            print(tuple(x))
            for i in range(len(x)):
                print(x[i])
            qprint("Book added")
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

# edit book {{{
class Ui_Dialog_Edit_Book(object):
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
        print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        x = []
        x.append(self.input_1.text())
        x.append(self.input_2.text())
        x.append(self.input_3.text())
        print("OK button clicked")
        if self.input_3.text() == '' or self.input_2.text() == '' or self.input_1.text() == '':
            err = f"Fields cannot be empty!"
            qprint(err)
        else:
            print(tuple(x))
            for i in range(len(x)):
                print(x[i])
            qprint("Book updated")
            self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit book"))
        self.the_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Edit a book's informations</span></p></body></html>"))
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
        print("Exit button clicked")
        self.Dialog.close()

    def ok_button_clicked(self):
        tmp = self.lineEdit.text()
        if tmp != '' and tmp != None:
            print(tmp)
        for button in self.buttonGroup1.buttons():
            if button.isChecked():
                print(button.text() + " is checked")

        for button in self.buttonGroup2.buttons():
            if button.isChecked():
                print(button.text() + " is checked")
        self.Dialog.close()

    # def check_buttons(self):
    #     for button in self.buttonGroup1.buttons():
    #         if button.isChecked():
    #             print(button.text() + " is checked")
    #
    #     for button in self.buttonGroup2.buttons():
    #         if button.isChecked():
    #             print(button.text() + " is checked")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Search book by:"))
        self.radioButton_3.setText(_translate("Dialog", "Book ID"))
        self.radioButton_4.setText(_translate("Dialog", "Publisher"))
        self.radioButton.setText(_translate("Dialog", "Book Name"))
        self.radioButton_2.setText(_translate("Dialog", "Author Name"))

        self.radioButton_5.setText(_translate("Dialog", "Delete"))
        self.radioButton_6.setText(_translate("Dialog", "View"))
        self.radioButton_7.setText(_translate("Dialog", "Edit"))

        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
# }}}

# delete book {{{

# }}}

# }}}

