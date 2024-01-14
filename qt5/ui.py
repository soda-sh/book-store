#!/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(789, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.HL_top = QtWidgets.QHBoxLayout()
        self.HL_top.setObjectName("HL_top")
        self.details_box = QtWidgets.QVBoxLayout()
        self.details_box.setObjectName("details_box")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        self.logo.setObjectName("logo")
        self.details_box.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setMaximumSize(QtCore.QSize(200, 200))
        self.text.setObjectName("text")
        self.details_box.addWidget(self.text, 0, QtCore.Qt.AlignHCenter)
        self.HL_top.addLayout(self.details_box)
        self.vline = QtWidgets.QFrame(self.centralwidget)
        self.vline.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline.setObjectName("vline")
        self.HL_top.addWidget(self.vline)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL_top.addItem(spacerItem)
        self.actions_box_1 = QtWidgets.QVBoxLayout()
        self.actions_box_1.setObjectName("actions_box_1")
        self.butt_books = QtWidgets.QPushButton(self.centralwidget)
        self.butt_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt_books.setObjectName("butt_books")
        self.actions_box_1.addWidget(self.butt_books)
        self.butt_users = QtWidgets.QPushButton(self.centralwidget)
        self.butt_users.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt_users.setObjectName("butt_users")
        self.actions_box_1.addWidget(self.butt_users)
        self.HL_top.addLayout(self.actions_box_1)
        self.actions_box_2 = QtWidgets.QVBoxLayout()
        self.actions_box_2.setObjectName("actions_box_2")
        self.butt_stack = QtWidgets.QPushButton(self.centralwidget)
        self.butt_stack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt_stack.setObjectName("butt_stack")
        self.actions_box_2.addWidget(self.butt_stack)
        self.butt_order = QtWidgets.QPushButton(self.centralwidget)
        self.butt_order.setObjectName("butt_order")
        self.actions_box_2.addWidget(self.butt_order)
        self.HL_top.addLayout(self.actions_box_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL_top.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL_top.addItem(spacerItem2)
        self.VL_state = QtWidgets.QVBoxLayout()
        self.VL_state.setObjectName("VL_state")
        self.butt_ok = QtWidgets.QPushButton(self.centralwidget)
        self.butt_ok.setObjectName("butt_ok")
        self.VL_state.addWidget(self.butt_ok)
        self.butt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_exit.setObjectName("butt_exit")
        self.VL_state.addWidget(self.butt_exit)
        self.HL_top.addLayout(self.VL_state)
        self.verticalLayout_4.addLayout(self.HL_top)
        self.hline = QtWidgets.QFrame(self.centralwidget)
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.verticalLayout_4.addWidget(self.hline)
        self.section_title = QtWidgets.QLabel(self.centralwidget)
        self.section_title.setObjectName("section_title")
        self.verticalLayout_4.addWidget(self.section_title)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)
        self.verticalLayout_4.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 37))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuDelete = QtWidgets.QMenu(self.menubar)
        self.menuDelete.setObjectName("menuDelete")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewBook = QtWidgets.QAction(MainWindow)
        self.actionNewBook.setObjectName("actionNewBook")
        self.actionNewUser = QtWidgets.QAction(MainWindow)
        self.actionNewUser.setObjectName("actionNewUser")
        self.actionDeleteBook = QtWidgets.QAction(MainWindow)
        self.actionDeleteBook.setObjectName("actionDeleteBook")
        self.actionDeleteUser = QtWidgets.QAction(MainWindow)
        self.actionDeleteUser.setObjectName("actionDeleteUser")
        self.actionEditBook = QtWidgets.QAction(MainWindow)
        self.actionEditBook.setObjectName("actionEditBook")
        self.actionEditUser = QtWidgets.QAction(MainWindow)
        self.actionEditUser.setObjectName("actionEditUser")
        self.actionNewOrder = QtWidgets.QAction(MainWindow)
        self.actionNewOrder.setObjectName("actionNewOrder")
        self.actionDeleteOrder = QtWidgets.QAction(MainWindow)
        self.actionDeleteOrder.setObjectName("actionDeleteOrder")
        self.actionDeleteStack = QtWidgets.QAction(MainWindow)
        self.actionDeleteStack.setObjectName("actionDeleteStack")
        self.actionNewStack = QtWidgets.QAction(MainWindow)
        self.actionNewStack.setObjectName("actionNewStack")
        self.actionEditOrder = QtWidgets.QAction(MainWindow)
        self.actionEditOrder.setObjectName("actionEditOrder")
        self.actionEditStack = QtWidgets.QAction(MainWindow)
        self.actionEditStack.setObjectName("actionEditStack")
        self.actionViewBook = QtWidgets.QAction(MainWindow)
        self.actionViewBook.setObjectName("actionViewBook")
        self.actionViewUser = QtWidgets.QAction(MainWindow)
        self.actionViewUser.setObjectName("actionViewUser")
        self.actionViewOrder = QtWidgets.QAction(MainWindow)
        self.actionViewOrder.setObjectName("actionViewOrder")
        self.actionViewStack = QtWidgets.QAction(MainWindow)
        self.actionViewStack.setObjectName("actionViewStack")
        self.menuNew.addAction(self.actionNewBook)
        self.menuNew.addAction(self.actionNewUser)
        self.menuNew.addAction(self.actionNewOrder)
        self.menuNew.addAction(self.actionNewStack)
        self.menuDelete.addAction(self.actionDeleteBook)
        self.menuDelete.addAction(self.actionDeleteUser)
        self.menuDelete.addAction(self.actionDeleteOrder)
        self.menuDelete.addAction(self.actionDeleteStack)
        self.menuEdit.addAction(self.actionEditBook)
        self.menuEdit.addAction(self.actionEditUser)
        self.menuEdit.addAction(self.actionEditOrder)
        self.menuEdit.addAction(self.actionEditStack)
        self.menuView.addAction(self.actionViewBook)
        self.menuView.addAction(self.actionViewUser)
        self.menuView.addAction(self.actionViewOrder)
        self.menuView.addAction(self.actionViewStack)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuDelete.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.actionViewBook.triggered.connect(self.books_button_clicked)

        # Connect functions to button clicks
        self.butt_books.clicked.connect(self.books_button_clicked)
        self.butt_users.clicked.connect(self.users_button_clicked)
        self.butt_order.clicked.connect(self.order_button_clicked)
        self.butt_stack.clicked.connect(self.stack_button_clicked)

        self.butt_exit.clicked.connect(self.exit_button_clicked)
        self.butt_ok.clicked.connect(self.ok_button_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_items_to_model(self, name):
        # Add items to the model (you can customize this based on your data)
        self.model.clear()
        self.model.setHorizontalHeaderLabels([f"{name} ID", f"Name"])

        for i in range(5):
            item1 = QtGui.QStandardItem(f"{name} {i + 1} - 1")
            item2 = QtGui.QStandardItem(f"{name} {i + 1} - 2")
            self.model.appendRow([item1, item2])

    def books_button_clicked(self):
        print("Books button clicked")
        self.section_title.setText("Books")
        self.add_items_to_model("Book") # Add items to the model

    def users_button_clicked(self):
        print("Users button clicked")
        self.section_title.setText("Users")
        self.add_items_to_model("User") # Add items to the model

    def stack_button_clicked(self):
        print("Stack button clicked")
        self.section_title.setText("Stack")
        self.add_items_to_model("Stack") # Add items to the model

    def order_button_clicked(self):
        print("Order button clicked")
        self.section_title.setText("Order List")
        self.add_items_to_model("Order") # Add items to the model

    def exit_button_clicked(self):
        print("Exit button clicked")
        QtWidgets.qApp.quit()

    def ok_button_clicked(self):
        print("OK button clicked")
        QtWidgets.qApp.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/mainlogo/logo.png\"/></p></body></html>"))
        self.text.setText(_translate("MainWindow", "Library app"))
        self.butt_books.setText(_translate("MainWindow", "Books"))
        self.butt_users.setText(_translate("MainWindow", "Users"))
        self.butt_stack.setText(_translate("MainWindow", "Stack"))
        self.butt_order.setText(_translate("MainWindow", "Order"))
        self.butt_ok.setText(_translate("MainWindow", "OK"))
        self.butt_exit.setText(_translate("MainWindow", "Exit"))
        self.section_title.setText(_translate("MainWindow", "Title"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuDelete.setTitle(_translate("MainWindow", "Delete"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNewBook.setText(_translate("MainWindow", "Book"))
        self.actionNewUser.setText(_translate("MainWindow", "User"))
        self.actionDeleteBook.setText(_translate("MainWindow", "Book"))
        self.actionDeleteUser.setText(_translate("MainWindow", "User"))
        self.actionEditBook.setText(_translate("MainWindow", "Book"))
        self.actionEditUser.setText(_translate("MainWindow", "User"))
        self.actionNewOrder.setText(_translate("MainWindow", "Order"))
        self.actionDeleteOrder.setText(_translate("MainWindow", "Order"))
        self.actionDeleteStack.setText(_translate("MainWindow", "Stack"))
        self.actionNewStack.setText(_translate("MainWindow", "Stack"))
        self.actionEditOrder.setText(_translate("MainWindow", "Order"))
        self.actionEditStack.setText(_translate("MainWindow", "Stack"))
        self.actionViewBook.setText(_translate("MainWindow", "Book"))
        self.actionViewUser.setText(_translate("MainWindow", "User"))
        self.actionViewOrder.setText(_translate("MainWindow", "Order"))
        self.actionViewStack.setText(_translate("MainWindow", "Stack"))
import figure_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
