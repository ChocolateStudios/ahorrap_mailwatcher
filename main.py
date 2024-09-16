import sys
from PyQt5.QtWidgets import QApplication
from qasync import QEventLoop
import asyncio

from app.widgets.app_manager import AppManager

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.manager = AppManager()
        self.setQuitOnLastWindowClosed(False)

if __name__ == '__main__':
    app = App(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    app.manager.show()

    with loop:
        loop.run_forever()

    sys.exit(app.exec_())