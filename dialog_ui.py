# Form implementation generated from reading ui file 'dialog_ui.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(234, 223)
        Dialog.setStyleSheet("")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 231, 199))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.error_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.error_label.setStyleSheet("QLabel {\n"
"color: #ff0000\n"
"}")
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.login_lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.verticalLayout.addWidget(self.login_lineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout.addWidget(self.password_lineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.site_lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.site_lineEdit.setObjectName("site_lineEdit")
        self.verticalLayout.addWidget(self.site_lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.horizontalLayout.addWidget(self.ok_pushButton)
        self.close_pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout.addWidget(self.close_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.error_label.setText(_translate("Dialog", "Введите"))
        self.label.setText(_translate("Dialog", "Введите логин:"))
        self.label_2.setText(_translate("Dialog", "Введите пароль:"))
        self.label_3.setText(_translate("Dialog", "Введите название сайта (необязательно):"))
        self.ok_pushButton.setText(_translate("Dialog", "OK"))
        self.close_pushButton.setText(_translate("Dialog", "Отмена"))
