# import sys
# import re
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtCore import Qt

# class RegisterScreen(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('AhorrApp\'e')
#         self.setFixedSize(320, 380)
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

#         title_label = QLabel("Registro")
#         title_label.setAlignment(Qt.AlignCenter)
#         title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
#         layout.addWidget(title_label)

#         self.email_input = QLineEdit()
#         self.email_input.setPlaceholderText("Correo electrónico")
#         layout.addWidget(self.email_input)

#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Contraseña")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         layout.addWidget(self.password_input)

#         self.confirm_password_input = QLineEdit()
#         self.confirm_password_input.setPlaceholderText("Confirmar contraseña")
#         self.confirm_password_input.setEchoMode(QLineEdit.Password)
#         layout.addWidget(self.confirm_password_input)

#         register_button = QPushButton("Registrarse")
#         register_button.setStyleSheet("""
#             QPushButton {
#                 background-color: #4CAF50;
#                 color: white;
#             }
#             QPushButton:hover {
#                 background-color: #45a049;
#             }
#         """)
#         register_button.clicked.connect(self.register)
#         layout.addWidget(register_button)

#         login_button = QPushButton("¿Ya tienes una cuenta? Inicia sesión")
#         login_button.setStyleSheet("""
#             QPushButton {
#                 background-color: transparent;
#                 color: #4CAF50;
#                 font-weight: normal;
#                 text-align: center;
#                 padding: 5px 0;
#             }
#             QPushButton:hover {
#                 text-decoration: underline;
#             }
#         """)
#         layout.addWidget(login_button)

#         self.setLayout(layout)

#     def register(self):
#         email = self.email_input.text()
#         password = self.password_input.text()
#         confirm_password = self.confirm_password_input.text()

#         if not email or not password or not confirm_password:
#             self.show_error("Por favor, complete todos los campos.")
#             return

#         if not self.validate_email(email):
#             self.show_error("Por favor, ingrese un correo electrónico válido.")
#             return

#         if len(password) < 8:
#             self.show_error("La contraseña debe tener al menos 8 caracteres.")
#             return

#         if password != confirm_password:
#             self.show_error("Las contraseñas no coinciden.")
#             return

#         QMessageBox.information(self, "Éxito", "Registro exitoso!")

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
#     register_screen = RegisterScreen()
#     register_screen.show()
#     sys.exit(app.exec_())



from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from screens.auth.styles.styles import get_styles

class RegisterScreen(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(get_styles())

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # Título
        title_label = QLabel("Registro")
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

        # Confirmar contraseña
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirmar contraseña")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_input)

        # Botón de registro
        self.register_button = QPushButton("Registrarse")
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        # self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        # Botones adicionales
        self.login_button = QPushButton("¿Ya tienes una cuenta? Inicia sesión")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #4CAF50;
                font-weight: normal;
                text-align: center;
                padding: 5px 0;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    # def register(self):
    #     email = self.email_input.text()
    #     password = self.password_input.text()
    #     confirm_password = self.confirm_password_input.text()

    #     if not email or not password or not confirm_password:
    #         self.show_error("Por favor, complete todos los campos.")
    #         return

    #     if not self.validate_email(email):
    #         self.show_error("Por favor, ingrese un correo electrónico válido.")
    #         return

    #     if len(password) < 8:
    #         self.show_error("La contraseña debe tener al menos 8 caracteres.")
    #         return

    #     if password != confirm_password:
    #         self.show_error("Las contraseñas no coinciden.")
    #         return

    #     QMessageBox.information(self, "Éxito", "Registro exitoso!")

    # def validate_email(self, email):
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     return re.match(pattern, email) is not None

    # def show_error(self, message):
    #     error_box = QMessageBox()
    #     error_box.setIcon(QMessageBox.Warning)
    #     error_box.setText(message)
    #     error_box.setWindowTitle("Error")
    #     error_box.setStyleSheet("""
    #         QMessageBox {
    #             background-color: #f0f0f0;
    #         }
    #         QMessageBox QLabel {
    #             color: #333;
    #         }
    #         QMessageBox QPushButton {
    #             background-color: #4CAF50;
    #             color: white;
    #             padding: 5px 15px;
    #             border-radius: 3px;
    #         }
    #         QMessageBox QPushButton:hover {
    #             background-color: #45a049;
    #         }
    #     """)
    #     error_box.exec_()