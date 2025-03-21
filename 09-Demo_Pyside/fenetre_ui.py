# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetre.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(956, 678)
        self.ed_nombre1 = QLineEdit(Form)
        self.ed_nombre1.setObjectName(u"ed_nombre1")
        self.ed_nombre1.setGeometry(QRect(220, 100, 113, 22))
        self.ed_nombre2 = QLineEdit(Form)
        self.ed_nombre2.setObjectName(u"ed_nombre2")
        self.ed_nombre2.setGeometry(QRect(220, 140, 113, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 100, 49, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 140, 49, 16))
        self.btnValider = QPushButton(Form)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(240, 190, 75, 24))
        self.lblResultat = QLabel(Form)
        self.lblResultat.setObjectName(u"lblResultat")
        self.lblResultat.setGeometry(QRect(250, 240, 49, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 40, 49, 16))
        self.champsSaisie = QPlainTextEdit(Form)
        self.champsSaisie.setObjectName(u"champsSaisie")
        self.champsSaisie.setGeometry(QRect(440, 330, 441, 211))
        self.btnLecture = QPushButton(Form)
        self.btnLecture.setObjectName(u"btnLecture")
        self.btnLecture.setGeometry(QRect(500, 560, 111, 24))
        self.btnEcriture = QPushButton(Form)
        self.btnEcriture.setObjectName(u"btnEcriture")
        self.btnEcriture.setGeometry(QRect(684, 560, 131, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre1:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre2:", None))
        self.btnValider.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.lblResultat.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Demo", None))
        self.btnLecture.setText(QCoreApplication.translate("Form", u"Lecture Fichier", None))
        self.btnEcriture.setText(QCoreApplication.translate("Form", u"Ecriture Fichier", None))
    # retranslateUi

