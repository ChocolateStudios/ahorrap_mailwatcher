from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from assets.assets import app_icon

class SystemTray(QSystemTrayIcon):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        self.setup_tray()

    def setup_tray(self):
        self.setIcon(QIcon(app_icon))
        # self.setIcon(QIcon.fromTheme("folder"))
        
        menu = QMenu()

        show_hide_action = QAction("Mostrar/Ocultar", self)
        show_hide_action.triggered.connect(self.toggle_window)
        menu.addAction(show_hide_action)

        quit_action = QAction("Salir", self)
        quit_action.triggered.connect(self.app_manager.quit_application)
        menu.addAction(quit_action)

        self.setContextMenu(menu)

        self.activated.connect(self.on_tray_activated)

    def toggle_window(self):
        if self.app_manager.isVisible():
            self.app_manager.hide()
        else:
            # self.app_manager.show()
            self.app_manager.show_above_tray_icon()

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.toggle_window()

    def show_message(self, title, message):
        self.showMessage(title, message, QIcon(app_icon))