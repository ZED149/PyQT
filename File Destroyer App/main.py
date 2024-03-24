

from PyQt6.QtWidgets import QApplication, QPushButton, QWidget
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QFileDialog, QHBoxLayout
from PyQt6.QtCore import Qt
from pathlib import Path


# Global variables
FILENAMES = ""


# our functions
def select_files():
    # we need to open a file browser
    # a file browser in QT is known as QFileDialog()
    global FILENAMES
    FILENAMES, _ = QFileDialog.getOpenFileNames()
    # setting message label text to Filenames
    message_label.setText("\n".join(FILENAMES))


def destroy_files():
    # iterating on filenames
    for filename in FILENAMES:
        path = Path(filename)
        # writing byte to file
        with open(path, 'wb') as file:
            file.write(b'')
        # unlinking the file from os
        path.unlink()
    # setting message label text to success
    message_label.setText("<font color='green'>All Files Deleted Successfully.</font>")


# initializing our app
app = QApplication([])

# creating window
window = QWidget()
# setting window title
window.setWindowTitle('ZED File Destroyer')

# creating layout(s)
main_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()

# creating text label
text = QLabel("Select files that you want to <font color='red'>permanently</font> delete.")
# adding text to main layout
main_layout.addWidget(text)

# adding buttons layout the main layout
main_layout.addLayout(buttons_layout)

# creating open files button
open_files_btn = QPushButton("Open Files")
open_files_btn.setText("Open Files")
# setting width of btn
open_files_btn.setFixedWidth(100)
# adding btn to main layout
buttons_layout.addWidget(open_files_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
# binding open_files button with select_files function
open_files_btn.clicked.connect(select_files)

# creating destroy files button
destroy_files_btn = QPushButton("Destroy Files")
# setting width of btn
destroy_files_btn.setFixedWidth(100)
# adding it to the main layout
buttons_layout.addWidget(destroy_files_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
# binding destroy files button to the function destroy files
destroy_files_btn.clicked.connect(destroy_files)

# creating message label
message_label = QLabel("")
# adding message label to main layout
main_layout.addWidget(message_label, alignment=Qt.AlignmentFlag.AlignHCenter)


# adding layout to window
window.setLayout(main_layout)
# showing window
window.show()
# executing our app
app.exec()
