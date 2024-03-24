
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QToolTip, QLineEdit
from PyQt6.QtCore import Qt
from pathlib import Path
import json


# our functions
def search():
    """
    Search English definition for the prompted word.
    :return:
    """
    search_word = word.text()
    search_word = search_word.lower()
    # now we need to look it into the JSON file
    path = Path("data.json")
    data_dict = ""
    with open("data.json", "r") as file:
        data_dict = json.load(file)

    if search_word in data_dict:
        result = data_dict[search_word]
        message = QLabel("\n".join(result))
        main_layout.addWidget(message)
    else:
        message = QLabel("<font color='red'>Word not found.</font>")
        message.setFixedSize(500, 50)
        main_layout.addWidget(message)


# initializing our app
app = QApplication([])

# creating our window
window = QWidget()
# setting title of window
window.setWindowTitle('ZED English Dictionary Desktop App')

# creating layout(s)
# creating main layout
main_layout = QVBoxLayout()
# creating inner_layout
inner_layout = QHBoxLayout()

# creating text box for word
word = QLineEdit()
# adding it to the main layout
inner_layout.addWidget(word, alignment=Qt.AlignmentFlag.AlignHCenter)

# creating search button
search_btn = QPushButton('Search')
# setting width of btn
search_btn.setFixedWidth(100)
# adding it to the main layout
inner_layout.addWidget(search_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
# binding search function to the button
search_btn.clicked.connect(search)


# adding inner layout to the main layout
main_layout.addLayout(inner_layout)

# adding main layout to window
window.setLayout(main_layout)
# showing window
window.show()
# executing our app
app.exec()
