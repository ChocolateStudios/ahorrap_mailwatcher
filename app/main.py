import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación de Escritorio con PyQt")
        self.setGeometry(100, 100, 600, 400)
        
        label = QLabel("Hola, mundo!", self)
        label.move(200, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())