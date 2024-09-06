from PyQt5.QtWidgets import QStackedWidget, QMainWindow
from screens.auth.login_screen import LoginScreen
from screens.auth.recover_screen import RecoverScreen
from screens.auth.register_screen import RegisterScreen
from screens.main.home_screen import HomeScreen

class AppManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AhorrApp\'e')
        self.setFixedSize(320, 380)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_screen = LoginScreen()
        self.recover_screen = RecoverScreen()
        self.register_screen = RegisterScreen()
        self.home_screen = HomeScreen()

        self.central_widget.addWidget(self.login_screen)
        self.central_widget.addWidget(self.recover_screen)
        self.central_widget.addWidget(self.register_screen)
        self.central_widget.addWidget(self.home_screen)

        self.setup_connections()

    def setup_connections(self):
        # Connect login screen buttons
        self.login_screen.forgot_password_button.clicked.connect(self.show_recover_screen)
        self.login_screen.register_button.clicked.connect(self.show_register_screen)
        self.login_screen.login_button.clicked.connect(self.handle_login)

        # Connect recover screen buttons
        self.recover_screen.login_button.clicked.connect(self.show_login_screen)

        # Connect register screen buttons
        self.register_screen.login_button.clicked.connect(self.show_login_screen)

        self.home_screen.logout_button.clicked.connect(self.handle_logout)
        self.home_screen.settings_button.clicked.connect(self.show_settings)

    def show_login_screen(self):
        self.central_widget.setCurrentWidget(self.login_screen)

    def show_recover_screen(self):
        self.central_widget.setCurrentWidget(self.recover_screen)

    def show_register_screen(self):
        self.central_widget.setCurrentWidget(self.register_screen)

    def show_home_screen(self):
        self.central_widget.setCurrentWidget(self.home_screen)

    def handle_login(self):
        # Aquí iría la lógica de autenticación
        # Si la autenticación es exitosa, mostrar la pantalla principal
        self.show_home_screen()

    def handle_logout(self):
        # Aquí iría la lógica de cierre de sesión
        self.show_login_screen()

    def show_settings(self):
        # Aquí iría la lógica para mostrar la pantalla de ajustes
        # Por ahora, simplemente imprimimos un mensaje
        print("Mostrando ajustes...")