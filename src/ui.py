#!/bin/python

from PyQt5 import QtCore, QtGui, QtWidgets
from database import database

from dialogs import Ui_Dialog_Add_Book as AddBook
from dialogs import Ui_Dialog_Add_User as AddUser
from dialogs import Ui_Dialog_Add_Stack as AddStack

from dialogs import Ui_Dialog_Search_Book as SearchBook
from dialogs import Ui_Dialog_Search_User as SearchUser
from dialogs import Ui_Dialog_Search_Stack as SearchStack

from dialogs import Ui_Dialog_Main_View_Book as ViewBook
from dialogs import Ui_Dialog_Main_View_User as ViewUser
from dialogs import Ui_Dialog_Main_View_Stack as ViewStack


db = database("test")

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
        self.butt_lend = QtWidgets.QPushButton(self.centralwidget)
        self.butt_lend.setObjectName("butt_lend")
        self.actions_box_2.addWidget(self.butt_lend)
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
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Make the table non-editable
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.tableView.setModel(self.model)
        self.verticalLayout_4.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 37))
        self.menubar.setObjectName("menubar")

        # new{{{
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")

        self.actionNewBook = QtWidgets.QAction(MainWindow)
        self.actionNewBook.setObjectName("actionNewBook")

        self.actionNewUser = QtWidgets.QAction(MainWindow)
        self.actionNewUser.setObjectName("actionNewUser")

        self.actionNewLend = QtWidgets.QAction(MainWindow)
        self.actionNewLend.setObjectName("actionNewLend")

        self.menubar.addAction(self.menuNew.menuAction())
        self.menuNew.addAction(self.actionNewBook)
        self.menuNew.addAction(self.actionNewUser)
        self.menuNew.addAction(self.actionNewLend)
        # }}}

        # # edit{{{
        # self.menuEdit = QtWidgets.QMenu(self.menubar)
        # self.menuEdit.setObjectName("menuEdit")

        # self.actionEditBook = QtWidgets.QAction(MainWindow)
        # self.actionEditBook.setObjectName("actionEditBook")

        # self.actionEditUser = QtWidgets.QAction(MainWindow)
        # self.actionEditUser.setObjectName("actionEditUser")

        # self.menubar.addAction(self.menuEdit.menuAction())
        # self.menuEdit.addAction(self.actionEditBook)
        # self.menuEdit.addAction(self.actionEditUser)
        # # }}}

        # search{{{
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")

        self.actionSearchBook = QtWidgets.QAction(MainWindow)
        self.actionSearchBook.setObjectName("actionSearchBook")

        self.actionSearchUser = QtWidgets.QAction(MainWindow)
        self.actionSearchUser.setObjectName("actionSearchUser")

        self.actionSearchStack = QtWidgets.QAction(MainWindow)
        self.actionSearchStack.setObjectName("actionSearchStack")

        self.menubar.addAction(self.menuSearch.menuAction())
        self.menuSearch.addAction(self.actionSearchBook)
        self.menuSearch.addAction(self.actionSearchUser)
        self.menuSearch.addAction(self.actionSearchStack)
        # }}}

        # signals {{{

        # menu signals{{{
        self.actionNewUser.triggered.connect(self.menu_users_clicked_new)
        self.actionNewBook.triggered.connect(self.menu_books_clicked_new)
        self.actionNewLend.triggered.connect(self.menu_lend_clicked_new)

        self.actionSearchBook.triggered.connect(self.menu_books_clicked_search)
        self.actionSearchUser.triggered.connect(self.menu_users_clicked_search)
        self.actionSearchStack.triggered.connect(self.menu_stack_clicked_search)

        # self.actionEditUser.triggered.connect(self.menu_users_clicked_edit)
        # self.actionEditBook.triggered.connect(self.menu_books_clicked_edit)
        # }}}

        # button signals{{{
        self.butt_books.clicked.connect(self.books_button_clicked)
        self.butt_users.clicked.connect(self.users_button_clicked)
        self.butt_stack.clicked.connect(self.stack_button_clicked)
        self.butt_lend.clicked.connect(self.lend_button_clicked)

        self.butt_exit.clicked.connect(self.exit_button_clicked)
        self.butt_ok.clicked.connect(self.ok_button_clicked)
        # }}}

        # }}}

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # signal functions {{{

    def books_button_clicked(self):
        name = "Books"
        cols = ["Name", "Author", "Publisher"]
        dialog = QtWidgets.QDialog()
        dialog.ui = ViewBook(name, cols)
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def users_button_clicked(self):
        name = "Users"
        cols = ["Name", "Address", "Phone NO."]
        dialog = QtWidgets.QDialog()
        dialog.ui = ViewUser(name, cols)
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def stack_button_clicked(self):
        name = "Stack"
        cols = ["User ID", "Book ID", "Add date"]
        dialog = QtWidgets.QDialog()
        dialog.ui = ViewStack(name, cols)
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def lend_button_clicked(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = AddStack()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def exit_button_clicked(self):
        QtWidgets.qApp.quit()

    def ok_button_clicked(self):
        QtWidgets.qApp.quit()

    def menu_users_clicked_search(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = SearchUser()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def menu_users_clicked_new(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = AddUser()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def menu_books_clicked_search(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = SearchBook()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def menu_books_clicked_new(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = AddBook()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def menu_stack_clicked_search(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = SearchStack()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def menu_lend_clicked_new(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = AddStack()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    # def menu_users_clicked_edit(self):
    #     dialog = QtWidgets.QDialog()
    #     dialog.ui = EditUser()
    #     dialog.ui.setupUi(dialog)
    #     dialog.exec_()

    # def menu_books_clicked_edit(self):
    #     dialog = QtWidgets.QDialog()
    #     dialog.ui = EditBook()
    #     dialog.ui.setupUi(dialog)
    #     dialog.exec_()

    # }}}

    # display texts
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # window title
        MainWindow.setWindowTitle(_translate("MainWindow", "Book Store"))
        # logo
        self.logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/mainlogo/logo.png\"/></p></body></html>"))
        # logo text
        self.text.setText(_translate("MainWindow", "Library app"))
        # buttons
        self.butt_books.setText(_translate("MainWindow", "Books"))
        self.butt_users.setText(_translate("MainWindow", "Users"))
        self.butt_stack.setText(_translate("MainWindow", "Stack"))
        # self.butt_lend.setText(_translate("MainWindow", ""))
        self.butt_lend.setText(_translate("MainWindow", "Lend"))
        self.butt_ok.setText(_translate("MainWindow", "OK"))
        self.butt_exit.setText(_translate("MainWindow", "Exit"))
        # table title
        self.section_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Title</span></p></body></html>"))

        # menu list
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.actionNewBook.setText(_translate("MainWindow", "Book"))
        self.actionNewUser.setText(_translate("MainWindow", "User"))
        self.actionNewLend.setText(_translate("MainWindow", "Lend"))

        # self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        # self.actionEditBook.setText(_translate("MainWindow", "Book"))
        # self.actionEditUser.setText(_translate("MainWindow", "User"))

        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.actionSearchBook.setText(_translate("MainWindow", "Book"))
        self.actionSearchUser.setText(_translate("MainWindow", "User"))
        self.actionSearchStack.setText(_translate("MainWindow", "Stack"))

# logo image
import figure_rc

# execute program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())














    """

    """