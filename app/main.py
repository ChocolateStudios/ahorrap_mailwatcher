import sys
from PyQt5.QtWidgets import QApplication
from widgets.app_manager import AppManager

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.manager = AppManager()
        self.setQuitOnLastWindowClosed(False)

if __name__ == '__main__':
    app = App(sys.argv)
    app.manager.show()
    sys.exit(app.exec_())