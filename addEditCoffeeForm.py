# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.le_title = QtWidgets.QLineEdit(Form)
        self.le_title.setObjectName("le_title")
        self.gridLayout.addWidget(self.le_title, 2, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.le_about = QtWidgets.QLineEdit(Form)
        self.le_about.setObjectName("le_about")
        self.gridLayout.addWidget(self.le_about, 5, 1, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.le_price = QtWidgets.QLineEdit(Form)
        self.le_price.setObjectName("le_price")
        self.gridLayout.addWidget(self.le_price, 6, 1, 1, 2)
        self.le_id = QtWidgets.QLineEdit(Form)
        self.le_id.setText("")
        self.le_id.setReadOnly(False)
        self.le_id.setPlaceholderText("")
        self.le_id.setObjectName("le_id")
        self.gridLayout.addWidget(self.le_id, 1, 1, 1, 2)
        self.le_roast_deg = QtWidgets.QLineEdit(Form)
        self.le_roast_deg.setObjectName("le_roast_deg")
        self.gridLayout.addWidget(self.le_roast_deg, 3, 1, 1, 2)
        self.le_volume = QtWidgets.QLineEdit(Form)
        self.le_volume.setObjectName("le_volume")
        self.gridLayout.addWidget(self.le_volume, 7, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 8, 0, 1, 3)
        self.le_type = QtWidgets.QLineEdit(Form)
        self.le_type.setObjectName("le_type")
        self.gridLayout.addWidget(self.le_type, 4, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Молотый/в зёрнах"))
        self.label_5.setText(_translate("Form", "Описание вкуса"))
        self.label.setText(_translate("Form", "ID"))
        self.label_6.setText(_translate("Form", "Цена"))
        self.label_2.setText(_translate("Form", "Название"))
        self.label_3.setText(_translate("Form", "Обжарка"))
        self.btn_save.setText(_translate("Form", "Сохранить"))
        self.label_7.setText(_translate("Form", "Объём упаковки"))
        self.label_8.setText(_translate("Form", "Введите существующий id для внесения изменений в запись\n"
"                            Введите новый id для создания новой записи\n"
"                        "))
