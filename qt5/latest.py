#!/bin/python

from PyQt5 import QtCore, QtGui, QtWidgets

# Class definition for the UI
class Ui_MainWindow(object):

    # Method to set up the UI components
    def setupUi(self, MainWindow):
        # Set up main window properties
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(789, 592)

        # Create central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a grid layout for central widget
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Create a vertical layout for the main components
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Create a horizontal layout for the top section
        self.HL_top = QtWidgets.QHBoxLayout()
        self.HL_top.setObjectName("HL_top")

        # Create a vertical layout for details box
        self.details_box = QtWidgets.QVBoxLayout()
        self.details_box.setObjectName("details_box")

        # Create a logo label
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        self.logo.setObjectName("logo")
        self.details_box.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)

        # Create a text label
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setMaximumSize(QtCore.QSize(200, 200))
        self.text.setObjectName("text")
        self.details_box.addWidget(self.text, 0, QtCore.Qt.AlignHCenter)

        # Add details box to top layout
        self.HL_top.addLayout(self.details_box)

        # Create a vertical line separator
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.HL_top.addWidget(self.line)

        # Create spacer items for layout flexibility
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL_top.addItem(spacerItem)

        # Create vertical layout for action buttons (1st set)
        self.actions_box_1 = QtWidgets.QVBoxLayout()
        self.actions_box_1.setObjectName("actions_box_1")

        # Create "Books" button
        self.butt_books = QtWidgets.QPushButton(self.centralwidget)
        self.butt_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt_books.setObjectName("butt_books")
        self.actions_box_1.addWidget(self.butt_books)

        # Create "Users" button
        self.butt_users = QtWidgets.QPushButton(self.centralwidget)
        self.butt_users.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt_users.setObjectName("butt_users")
        self.actions_box_1.addWidget(self.butt_users)

        # Add action buttons (1st set) to top layout
        self.HL_top.addLayout(self.actions_box_1)

        # Create vertical layout for action buttons (2nd set)
        self.actions_box_2 = QtWidgets.QVBoxLayout()
        self.actions_box_2.setObjectName("actions_box_2")

        # Create "Stack" button
        self.butt_stack = QtWidgets.QPushButton(self.centralwidget)
        self.butt_stack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt_stack.setObjectName("butt_stack")
        self.actions_box_2.addWidget(self.butt_stack)

        # Create "Order" button
        self.butt_order = QtWidgets.QPushButton(self.centralwidget)
        self.butt_order.setObjectName("butt_order")
        self.actions_box_2.addWidget(self.butt_order)

        # Add action buttons (2nd set) to top layout
        self.HL_top.addLayout(self.actions_box_2)

        # Create spacer items for layout flexibility
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL_top.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL_top.addItem(spacerItem2)

        # Create vertical layout for state buttons (e.g., OK, Exit)
        self.VL_state = QtWidgets.QVBoxLayout()
        self.VL_state.setObjectName("VL_state")

        # Create "OK" button
        self.butt_ok = QtWidgets.QPushButton(self.centralwidget)
        self.butt_ok.setObjectName("butt_ok")
        self.VL_state.addWidget(self.butt_ok)

        # Create "Exit" button
        self.butt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_exit.setObjectName("butt_exit")
        self.VL_state.addWidget(self.butt_exit)

        # Add state buttons to top layout
        self.HL_top.addLayout(self.VL_state)

        # Add top layout to main vertical layout
        self.verticalLayout_4.addLayout(self.HL_top)

        # Create a horizontal line separator
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        # Add the horizontal line separator to the main vertical layout
        self.verticalLayout_4.addWidget(self.line_2)

        # Create a QTableView
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")

        # Make the table non-editable
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Create a QStandardItemModel
        self.model = QtGui.QStandardItemModel()

        # Set the model for the QTableView
        self.tableView.setModel(self.model)

        # Add items to the model
        self.add_items_to_model()

        # Add the QTableView to the main vertical layout
        self.verticalLayout_4.addWidget(self.tableView)

        # Add the main vertical layout to the grid layout
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        # Set the central widget for the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Create menu bar, menus, and status bar
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

        # Set the menu bar for the main window
        MainWindow.setMenuBar(self.menubar)

        # Create and set the status bar for the main window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add menu actions to the menu bar
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuDelete.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.menuNew.triggered.connect(self.books_button_clicked)

        # Connect functions to button clicks
        self.butt_books.clicked.connect(self.books_button_clicked)
        self.butt_users.clicked.connect(self.users_button_clicked)
        self.butt_order.clicked.connect(self.order_button_clicked)
        self.butt_stack.clicked.connect(self.stack_button_clicked)
        self.butt_exit.clicked.connect(self.exit_button_clicked)

        # Translate UI components
        self.retranslateUi(MainWindow)

        # Connect slots by name
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Method to add items to the model (for the QTableView)
    def add_items_to_model(self):
        # Add items to the model (you can customize this based on your data)
        self.model.setHorizontalHeaderLabels(["Column 1", "Column 2"])

        for i in range(5):
            item1 = QtGui.QStandardItem(f"Item {i + 1} - Col 1")
            item2 = QtGui.QStandardItem(f"Item {i + 1} - Col 2")
            self.model.appendRow([item1, item2])

    # Methods for button click events
    def books_button_clicked(self):
        print("Books button clicked")

    def users_button_clicked(self):
        print("Users button clicked")

    def stack_button_clicked(self):
        print("Stack button clicked")

    def order_button_clicked(self):
        print("Order button clicked")

    def exit_button_clicked(self):
        print("Exit button clicked")
        QtWidgets.qApp.quit()

    # Method to translate UI components
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/mainlogo/logo.png\"/></p></body></html>"))
        self.text.setText(_translate("MainWindow", "Library app"))
        self.butt_books.setText(_translate("MainWindow", "Books"))
        self.butt_users.setText(_translate("MainWindow", "Users"))
        self.butt_stack.setText(_translate("MainWindow", "Stack"))
        self.butt_order.setText(_translate("MainWindow", "Order"))
        self.butt_exit.setText(_translate("MainWindow", "Exit"))
        self.butt_ok.setText(_translate("MainWindow", "OK"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuDelete.setTitle(_translate("MainWindow", "Delete"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))

# Import figure_rc module
import figure_rc

# Entry point of the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

