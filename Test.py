from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
yazı = QtWidgets.QLabel("Bu program Umut Can tarafından\n03 Ekim 2019 Perşembe 23.38'da yapılmıştır.\nBeta versiyonunu kullanmaktasınız.")
combo = QtWidgets.QComboBox(pencere)
combo.resize(50,50)
combo.addItems(["Kanal Seçin..",
             "Kanal D",
             "Fox Tv",
             "Show Tv",
             "Star Tv",
             "Atv",
             "Trt 1",
             "Tv8",
             "Kanal 7",
             "A Haber",
             "CNN Turk",
             "CNBC-e",
             "Kanalturk",
             "Samanyolu",
             "Ntv",
             "TNT",
             "Halk Tv",
             "GS Tv",
             "FB Tv",
             "BJK Tv",
             "Bursaspor Tv",
             "Ntvspor",
             "Ligtv"
             ])

text = QtWidgets.QTextBrowser(pencere)
text.clear()
about = "\nBu program Umut Can tarafından \n" \
                "\n03 Ekim 2019 Perşembe 23.38'da yapılmıştır.\n" \
                "\nBeta versiyonunu kullanmaktasınız."
text.append(about)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(combo)
vbox.addWidget(text)
vbox.addWidget(yazı)
vbox.addStretch()
hbox = QtWidgets.QHBoxLayout()
hbox.addLayout(vbox)
hbox.addStretch()

pencere.resize(300, 450)
pencere.setLayout(hbox)
pencere.show()



sys.exit(app.exec_())