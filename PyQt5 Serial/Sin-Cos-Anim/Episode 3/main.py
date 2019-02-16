import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.resize(1218, 722)
        # self.setStyleSheet("""#centralwidget {
            # background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(87, 255, 140, 255), stop:1 rgba(117, 210, 255, 255));
            # }"""
        # )
        
        # MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setText("Hello")
        self.button.clicked.connect(self.btnOnClicked)
        self.button.setStyleSheet(
            """
                /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));*/
                background-color: white;
                border-radius: 15px;
                border-radius:
                    30px;
                border-style:
                    solid;
                border-width:
                    10px;
                border-color: green;
                font: 63 20pt "Adobe 繁黑體 Std B";
            """
        )
        
        self.setCentralWidget(self.centralwidget)
        
    def btnOnClicked(self):
        print("Button 被按下了!")
        
app = None
window = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())