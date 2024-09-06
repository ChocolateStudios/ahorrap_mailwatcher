# import sys
# import re
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt

# class LoginScreen(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('AhorrApp\'e')
#         self.setFixedSize(320, 380)  # Aumentado ligeramente el ancho
#         self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
#         self.setStyleSheet("""
#             QWidget {
#                 background-color: #f0f0f0;
#                 font-family: 'Segoe UI', Arial, sans-serif;
#             }
#             QLineEdit {
#                 padding: 12px;
#                 border: 1px solid #ddd;
#                 border-radius: 4px;
#                 background-color: white;
#                 font-size: 14px;
#             }
#             QPushButton {
#                 padding: 12px;
#                 border: none;
#                 border-radius: 4px;
#                 font-size: 14px;
#                 font-weight: bold;
#             }
#         """)

#         layout = QVBoxLayout()
#         layout.setSpacing(15)
#         layout.setContentsMargins(30, 30, 30, 30)

#         # Título
#         title_label = QLabel("Iniciar Sesión")
#         title_label.setAlignment(Qt.AlignCenter)
#         title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
#         layout.addWidget(title_label)

#         # Correo electrónico
#         self.email_input = QLineEdit()
#         self.email_input.setPlaceholderText("Correo electrónico")
#         layout.addWidget(self.email_input)

#         # Contraseña
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Contraseña")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         layout.addWidget(self.password_input)

#         # Botón de inicio de sesión
#         login_button = QPushButton("Iniciar sesión")
#         login_button.setStyleSheet("""
#             QPushButton {
#                 background-color: #4CAF50;
#                 color: white;
#             }
#             QPushButton:hover {
#                 background-color: #45a049;
#             }
#         """)
#         login_button.clicked.connect(self.login)
#         layout.addWidget(login_button)

#         # Botones adicionales
#         additional_buttons_layout = QVBoxLayout()  # Cambiado a QVBoxLayout
#         additional_buttons_layout.setSpacing(5)  # Añadido espacio entre botones
#         forgot_password_button = QPushButton("¿Olvidaste tu contraseña?")
#         register_button = QPushButton("Registrarse")
        
#         for button in [forgot_password_button, register_button]:
#             button.setStyleSheet("""
#                 QPushButton {
#                     background-color: transparent;
#                     color: #4CAF50;
#                     font-weight: normal;
#                     text-align: left;
#                     padding: 5px 0;
#                 }
#                 QPushButton:hover {
#                     text-decoration: underline;
#                 }
#             """)
#             additional_buttons_layout.addWidget(button)
        
#         layout.addLayout(additional_buttons_layout)

#         self.setLayout(layout)

#     def login(self):
#         email = self.email_input.text()
#         password = self.password_input.text()

#         if not self.validate_email(email):
#             self.show_error("Por favor, ingrese un correo electrónico válido.")
#             return

#         if len(password) < 8:
#             self.show_error("La contraseña debe tener al menos 8 caracteres.")
#             return

#         # Aquí iría la lógica de autenticación real
#         QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso!")

#     def validate_email(self, email):
#         pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         return re.match(pattern, email) is not None

#     def show_error(self, message):
#         error_box = QMessageBox()
#         error_box.setIcon(QMessageBox.Warning)
#         error_box.setText(message)
#         error_box.setWindowTitle("Error")
#         error_box.setStyleSheet("""
#             QMessageBox {
#                 background-color: #f0f0f0;
#             }
#             QMessageBox QLabel {
#                 color: #333;
#             }
#             QMessageBox QPushButton {
#                 background-color: #4CAF50;
#                 color: white;
#                 padding: 5px 15px;
#                 border-radius: 3px;
#             }
#             QMessageBox QPushButton:hover {
#                 background-color: #45a049;
#             }
#         """)
#         error_box.exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     login_screen = LoginScreen()
#     login_screen.show()
#     sys.exit(app.exec_())





from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from screens.auth.styles.styles import get_screen_styles, get_main_button_styles, get_additional_buttons_styles

class LoginScreen(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(get_screen_styles())

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # Título
        title_label = QLabel("Iniciar Sesión")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(title_label)

        # Correo electrónico
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Correo electrónico")
        layout.addWidget(self.email_input)

        # Contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Botón de inicio de sesión
        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.setStyleSheet(get_main_button_styles())
        layout.addWidget(self.login_button)

        # Botones adicionales
        additional_buttons_layout = QVBoxLayout()
        additional_buttons_layout.setSpacing(5)
        self.forgot_password_button = QPushButton("¿Olvidaste tu contraseña?")
        self.register_button = QPushButton("Registrarse")
        
        for button in [self.forgot_password_button, self.register_button]:
            button.setStyleSheet(get_additional_buttons_styles())
            additional_buttons_layout.addWidget(button)
        
        layout.addLayout(additional_buttons_layout)

        self.setLayout(layout)