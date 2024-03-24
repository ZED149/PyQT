

from PyQt6.QtWidgets import QApplication, QLabel, QPushButton
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtWidgets import QComboBox, QHBoxLayout
from bs4 import BeautifulSoup
import requests


# out functions
def convert():
    amount = float(text.text())
    url = (f"https://www.x-rates.com/calculator/?from={input_currency_combobox.currentText()}&to={output_currency_combobox.currentText()}"
           f"&amount={amount}")
    # making a request to the url
    response = requests.get(url)

    # creating soup
    soup = BeautifulSoup(response.text, parser='html.parser', features="lxml")
    converted = soup.find(class_='ccOutputRslt').getText()
    message = f"{amount} {input_currency_combobox.currentText()} is {converted}."
    output_label.setText(message)


# initializing our app
app = QApplication([])

# creating our window
window = QWidget()
# setting window title
window.setWindowTitle('ZED Currency Converter')

# creating layout(s)
main_layout = QVBoxLayout()
layout_inner = QHBoxLayout()
layout_1 = QVBoxLayout()
layout_2 = QVBoxLayout()

# connecting layout to window
window.setLayout(main_layout)

main_layout.addLayout(layout_inner)
layout_inner.addLayout(layout_1)
layout_inner.addLayout(layout_2)


# adding widgets to layout
# input currency combobox
input_currency_combobox = QComboBox()
currencies = ['EUR', 'USD', 'GBP', 'PKR', 'JPY', 'RUB', 'CHF', 'INR']
input_currency_combobox.addItems(currencies)
# adding input currency combobox to layout
layout_1.addWidget(input_currency_combobox)

# output currency combobox
output_currency_combobox = QComboBox()
output_currency_combobox.addItems(currencies)
# adding output currency combobox to layout
layout_1.addWidget(output_currency_combobox)

# adding textbox to layout
text = QLineEdit()
layout_2.addWidget(text)

# adding convert button to layout
btn = QPushButton('Convert')
layout_2.addWidget(btn)

# adding output label to layout
output_label = QLabel("")
main_layout.addWidget(output_label)

# now, binding a function with our button click signal
btn.clicked.connect(convert)

# showing windows
window.show()

# executing our app
app.exec()
