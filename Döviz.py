from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QLabel,QPushButton,QApplication,QWidget,QMainWindow,qApp
import sys
from bs4 import BeautifulSoup
import requests

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.veri_cek()
        self.init_ui()

    def init_ui(self):


        self.gram_altın = QLabel("GRAM ALTIN : " + self.gram_altın_deger)
        self.dolar = QLabel("DOLAR :" + self.dolar_deger )
        self.euro = QLabel("EURO : " + self.euro_deger)
        self.btc = QLabel("BİTCOİN : " + self.btc_deger)
        self.buton_güncelle = QPushButton("Güncelle")
        self.buton_cıkıs = QPushButton("Çıkış")

        h_box = QHBoxLayout()
        h_box.addWidget(self.buton_güncelle)
        h_box.addWidget(self.buton_cıkıs)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.gram_altın)
        v_box.addWidget(self.dolar)
        v_box.addWidget(self.euro)
        v_box.addWidget(self.btc)
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.buton_cıkıs.clicked.connect(self.click)
        self.buton_güncelle.clicked.connect(self.click)
        self.setWindowTitle("Döviz Değerleri")
        self.setLayout(v_box)
        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Çıkış":
            qApp.exit()
        else:
            self.veri_cek()
            self.init_ui()





    def veri_cek(self):
        self.url = "https://www.doviz.com/"
        self.response = requests.get(self.url)
        self.html_icerik = self.response.content
        self.doviz_cins_list = list()
        self.doviz_deger_list = list()

        self.soup = BeautifulSoup(self.html_icerik,"html.parser")

        self.doviz_cins = self.soup.find_all("span",{"class":"name"})
        self.doviz_deger = self.soup.find_all("span",{"class":"value"})

        for i,j in zip(self.doviz_cins,self.doviz_deger):
            self.doviz_cins_list.append(i.text)
            self.doviz_deger_list.append(j.text)

        self.gram_altın_deger = self.doviz_deger_list[0]
        self.dolar_deger = self.doviz_deger_list[1]
        self.euro_deger = self.doviz_deger_list[2]
        self.btc_deger = self.doviz_deger_list[5]


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())