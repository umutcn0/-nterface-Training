from bs4 import BeautifulSoup
import requests
from PyQt5 import QtWidgets
import sys
from datetime import date


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.arayüz()
        self.soup("https://www.tvyayinakisi.com/kanal-d-tv-yayin-akisi")


    def arayüz(self):
        self.about ="\nBu program Umut Can tarafından \
                    \n03 Ekim 2019 Perşembe 23.38'da yapılmıştır \
                    \nBeta versiyonunu kullanmaktasınız."

        self.yapımcı = QtWidgets.QLabel(self.about)
        self.text_browser = QtWidgets.QTextBrowser()
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItems(["Kanal Seçin..",
             "Kanal D",
             "Fox Tv",
             "Show Tv",
             "Star Tv",
             "Atv",
             "Trt 1",
             "Tv8",
             "Teve 2",
             "BEYAZ TV",
             "A2",
             "TV 8,5",
             "Cartoon Network",
             ])

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.combo)
        vbox.addWidget(self.text_browser)
        vbox.addWidget(self.yapımcı)
        vbox.addStretch()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch()


        self.combo.currentIndexChanged.connect(self.click)


        self.setLayout(hbox)
        self.show()

    def click(self):
        if self.combo.currentIndex() == 0:
            self.text_browser.clear()
            self.text_browser.setText("Kanal Seçiniz")

        elif self.combo.currentIndex() == 1 :
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/kanal-d-tv-yayin-akisi"))

        elif self.combo.currentIndex() == 2:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/fox-yayin-akisi"))

        elif self.combo.currentIndex() == 3:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/show-tv-yayin-akisi"))

        elif self.combo.currentIndex() == 4:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/star-tv-yayin-akisi"))

        elif self.combo.currentIndex() == 5:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/atv-yayin-akisi"))

        elif self.combo.currentIndex() == 6:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/trt-1-yayin-akisi"))

        elif self.combo.currentIndex() == 7:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/tv-8-yayin-akisi"))

        elif self.combo.currentIndex() == 8:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/teve2-yayin-akisi"))

        elif self.combo.currentIndex() == 9:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/beyaz-tv-yayin-akisi"))

        elif self.combo.currentIndex() == 10:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/a2-yayin-akisi"))

        elif self.combo.currentIndex() == 11:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/tv-85-yayin-akisi"))

        elif self.combo.currentIndex() == 12:
            self.text_browser.clear()
            self.text_browser.setText(self.soup("https://www.tvyayinakisi.com/cartoon-network-yayin-akisi"))

        else :
            self.text_browser.clear()
            self.text_browser.setText("Seçim Yapınız.")

    def soup(self,url):
        prog_liste = ""
        response = requests.get(url)
        html_icerik = response.content

        soup = BeautifulSoup(html_icerik,"html.parser")
        saat = soup.find_all("p", {"class" : "time"})
        program = soup.find_all("p" ,{"class" : "name"})

        for i,j in zip(saat,program):
             prog_liste += i.text + "  " + j.text + "\n"

        return prog_liste



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()


sys.exit(app.exec_())







