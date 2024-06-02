from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


# Function to show a message box
def show_message():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Hello, PyQt5!")
    msg.setWindowTitle("Message")
    msg.exec_()


# Create the application and main window
app = QApplication([])
window = QWidget()
window.setWindowTitle('Basic GUI with PyQt5')
window.setGeometry(100, 100, 400, 300)

# Create a button and attach the function
button = QPushButton('Click Me', window)
button.clicked.connect(show_message)
button.move(150, 130)

# Show the window and run the application
window.show()
app.exec_()
