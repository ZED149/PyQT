

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

# OUR FUNCTIONS
def make_sentence():
    text_input = text.text()
    output_label.setText(text_input.capitalize() + '.')



# initializing our app
app = QApplication([])

# creating window
window = QWidget()
# setting window title
window.setWindowTitle('ZED Curreccy Converter')

# creating layout
layout = QVBoxLayout()
# adding textbox widget to layout
text = QLineEdit()
layout.addWidget(text)

# adding button to layout
btn = QPushButton("Make")
layout.addWidget(btn)

# output label
output_label = QLabel("")
layout.addWidget(output_label)

# handling click signal for button
btn.clicked.connect(make_sentence)


# connecting layout to window
window.setLayout(layout)
window.show()


# executing our app
app.exec()

