import sys
from PyQt5 import QtWidgets,QtGui
import sqlite3
import time

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.k_database = database()
        self.uygulama()

    def uygulama(self):

        self.k_adı = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buton_giris = QtWidgets.QPushButton("Giriş Yap")
        self.buton_kayıt_ol = QtWidgets.QPushButton("Kayıt ol")
        self.k_adı_text = QtWidgets.QLabel("Kullanıcı Adı : ")
        self.sifre_text = QtWidgets.QLabel("Şifre : ")
        self.durum = QtWidgets.QLabel("Giriş Yapınız...")

        k_box = QtWidgets.QVBoxLayout()
        k_box.addWidget(self.k_adı_text)
        k_box.addWidget(self.sifre_text)
        k_box.addStretch()

        button_box = QtWidgets.QHBoxLayout()
        button_box.addWidget(self.buton_giris)
        button_box.addWidget(self.buton_kayıt_ol)
        button_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.k_adı)
        v_box.addWidget(self.sifre)
        v_box.addLayout(button_box)
        v_box.addWidget(self.durum)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addLayout(k_box)
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.buton_giris.clicked.connect(self.click)
        self.buton_kayıt_ol.clicked.connect(self.click)

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.show()

    def click(self):
        sender = self.sender()
        k_adı = self.k_adı.text()
        sifre = self.sifre.text()

        if sender.text() =="Giriş Yap":

            if self.k_database.veri_kontrol(k_adı,sifre) == False:
                self.durum.setText("Böyle bir kullanıcı bulunamadı..")
            else:
                self.durum.setText("Giriş Başarılı :)")
        else:
            self.kayıtol = pencere_kayıt()
            self.durum.setText("Kayıt Başarılı. Lütfen tekrar giriş yapın")

class database():
    def __init__(self):
        self.database()

    def database(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS database (k_adı TEXT,sifre TEXT)")
        self.db.commit()

    def veri_ekle(self,k_adı,sifre):
        self.cursor.execute("INSERT INTO database VALUES(?,?)",(k_adı,sifre))
        self.db.commit()
        self.db.close()

    def veri_kontrol(self,k_adı,sifre):
        self.cursor.execute("Select * From database where k_adı = ? and sifre = ?",(k_adı,sifre))
        kontrol = self.cursor.fetchall()
        if len(kontrol) == 0:
            return False
        else:
            return True


class pencere_kayıt(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.kayıt_ol()

    def kayıt_ol(self):
        self.k_adı = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buton_tamamla = QtWidgets.QPushButton("Kaydı Tamamla")
        self.k_adı_text = QtWidgets.QLabel("Kullanıcı Adı : ")
        self.sifre_text = QtWidgets.QLabel("Şifre : ")
        self.durum = QtWidgets.QLabel("Kayıt için Formu Doldurunuz....")


        v2_box = QtWidgets.QVBoxLayout()
        v2_box.addWidget(self.k_adı_text)
        v2_box.addWidget(self.sifre_text)
        v2_box.addStretch()

        v_box= QtWidgets.QVBoxLayout()
        v_box.addWidget(self.k_adı)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.buton_tamamla)
        v_box.addWidget(self.durum)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addLayout(v2_box)
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.buton_tamamla.clicked.connect(self.kontrol)

        
        self.setWindowTitle("Kayıt Ol")
        self.setLayout(h_box)
        self.show()


    def kontrol(self):
        self.okay = bool()
        self.k_database = database()
        self.k_database.veri_ekle(self.k_adı.text(),self.sifre.text())
        self.durum.setText("Kayıt tamamlandı.")
        self.okay = True






app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())






