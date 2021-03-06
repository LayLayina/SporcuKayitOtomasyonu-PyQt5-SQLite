# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Sporcu Kayıt Uygulaması")
        MainWindow.resize(941, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 681, 331))
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(320, 20, 101, 16))
        self.label_9.setObjectName("label_9")
        self.cwDTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwDTarihi.setGeometry(QtCore.QRect(320, 40, 351, 261))
        self.cwDTarihi.setObjectName("cwDTarihi")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 279, 192))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lneTCK = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneTCK.setMaxLength(11)
        self.lneTCK.setObjectName("lneTCK")
        self.horizontalLayout.addWidget(self.lneTCK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lneSporcuAdi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneSporcuAdi.setObjectName("lneSporcuAdi")
        self.horizontalLayout_2.addWidget(self.lneSporcuAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lneSporcuSoyadi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneSporcuSoyadi.setObjectName("lneSporcuSoyadi")
        self.horizontalLayout_3.addWidget(self.lneSporcuSoyadi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.cmbSporKulb = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbSporKulb.setObjectName("cmbSporKulb")
        self.cmbSporKulb.addItem("")
        self.cmbSporKulb.addItem("")
        self.cmbSporKulb.addItem("")
        self.cmbSporKulb.addItem("")
        self.cmbSporKulb.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbSporKulb)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spnKilo = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnKilo.setMinimum(50)
        self.spnKilo.setMaximum(130)
        self.spnKilo.setObjectName("spnKilo")
        self.horizontalLayout_5.addWidget(self.spnKilo)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.cmbCinsiyet = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.cmbCinsiyet.addItem("")
        self.cmbCinsiyet.addItem("")
        self.horizontalLayout_6.addWidget(self.cmbCinsiyet)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.chkMedeniHal = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkMedeniHal.setObjectName("chkMedeniHal")
        self.horizontalLayout_7.addWidget(self.chkMedeniHal)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.lwBrans = QtWidgets.QListWidget(self.groupBox)
        self.lwBrans.setGeometry(QtCore.QRect(60, 240, 241, 91))
        self.lwBrans.setObjectName("lwBrans")
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.label_8.setObjectName("label_8")
        self.tblwBilgiler = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwBilgiler.setGeometry(QtCore.QRect(20, 380, 891, 261))
        self.tblwBilgiler.setRowCount(100)
        self.tblwBilgiler.setColumnCount(10)
        self.tblwBilgiler.setObjectName("tblwBilgiler")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(730, 30, 181, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_2.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_2.addWidget(self.btnSil)
        self.btnAra = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_2.addWidget(self.btnAra)
        self.btnGuncelle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_2.addWidget(self.btnGuncelle)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_2.addWidget(self.btnListele)
        self.btnCiks = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnCiks.setObjectName("btnCiks")
        self.verticalLayout_2.addWidget(self.btnCiks)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 650, 111, 21))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.lblkayitsayisi = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblkayitsayisi.setFont(font)
        self.lblkayitsayisi.setText("")
        self.lblkayitsayisi.setObjectName("lblkayitsayisi")
        self.horizontalLayout_8.addWidget(self.lblkayitsayisi)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(710, 660, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lblOrtKilo = QtWidgets.QLabel(self.centralwidget)
        self.lblOrtKilo.setGeometry(QtCore.QRect(810, 660, 51, 21))
        self.lblOrtKilo.setText("")
        self.lblOrtKilo.setObjectName("lblOrtKilo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menhakinda = QtWidgets.QAction(MainWindow)
        self.menhakinda.setObjectName("menhakinda")
        self.menuYard_m.addAction(self.menhakinda)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbSporKulb.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Sporcu Bilgileri"))
        self.label_9.setText(_translate("MainWindow", "Doğum Tarihi:"))
        self.label.setText(_translate("MainWindow", "Tc Kimlik Numarası:"))
        self.label_2.setText(_translate("MainWindow", "Sporcu Adı:"))
        self.label_3.setText(_translate("MainWindow", "Sporcu Soyad:ı"))
        self.label_4.setText(_translate("MainWindow", "Spor Kulübü:"))
        self.cmbSporKulb.setItemText(0, _translate("MainWindow", "Galatasaray"))
        self.cmbSporKulb.setItemText(1, _translate("MainWindow", "Beşiktaş"))
        self.cmbSporKulb.setItemText(2, _translate("MainWindow", "Fenerbahçe"))
        self.cmbSporKulb.setItemText(3, _translate("MainWindow", "TrabzonSpor"))
        self.cmbSporKulb.setItemText(4, _translate("MainWindow", "Başakşehir"))
        self.label_5.setText(_translate("MainWindow", "Sporcu Kilosu:"))
        self.label_6.setText(_translate("MainWindow", "Sporcu Cinsiyet:"))
        self.cmbCinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmbCinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_7.setText(_translate("MainWindow", "Medeni Hali:"))
        self.chkMedeniHal.setText(_translate("MainWindow", "Evli"))
        __sortingEnabled = self.lwBrans.isSortingEnabled()
        self.lwBrans.setSortingEnabled(False)
        item = self.lwBrans.item(0)
        item.setText(_translate("MainWindow", "Güreş"))
        item = self.lwBrans.item(1)
        item.setText(_translate("MainWindow", "Box"))
        item = self.lwBrans.item(2)
        item.setText(_translate("MainWindow", "Karate"))
        item = self.lwBrans.item(3)
        item.setText(_translate("MainWindow", "Tekvando"))
        item = self.lwBrans.item(4)
        item.setText(_translate("MainWindow", "Futbol"))
        self.lwBrans.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Branş:"))
        self.btnEkle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.btnSil.setText(_translate("MainWindow", "KAYIT SİL"))
        self.btnAra.setText(_translate("MainWindow", "KAYIT ARA"))
        self.btnGuncelle.setText(_translate("MainWindow", "GÜNCELLE"))
        self.btnListele.setText(_translate("MainWindow", "KAYIT LİSTELE"))
        self.btnCiks.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.label_10.setText(_translate("MainWindow", "Kayıt Sayısı:"))
        self.label_11.setText(_translate("MainWindow", "Kilo Ortalaması:"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.menhakinda.setText(_translate("MainWindow", "Hakkında"))
