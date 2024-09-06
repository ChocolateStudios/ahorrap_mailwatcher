# import sys
# import re
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtCore import Qt

# class RecoverScreen(QWidget):
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
#         layout.setSpacing(20)
#         layout.setContentsMargins(30, 30, 30, 30)

#         title_label = QLabel("Recuperar Contraseña")
#         title_label.setAlignment(Qt.AlignCenter)
#         title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
#         layout.addWidget(title_label)

#         instruction_label = QLabel("Ingresa tu correo electrónico y te enviaremos instrucciones para restablecer tu contraseña.")
#         instruction_label.setWordWrap(True)
#         instruction_label.setStyleSheet("font-size: 14px; color: #555; margin-bottom: 10px;")
#         instruction_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(instruction_label)

#         self.email_input = QLineEdit()
#         self.email_input.setPlaceholderText("Correo electrónico")
#         layout.addWidget(self.email_input)

#         recover_button = QPushButton("Enviar instrucciones")
#         recover_button.setStyleSheet("""
#             QPushButton {
#                 background-color: #4CAF50;
#                 color: white;
#             }
#             QPushButton:hover {
#                 background-color: #45a049;
#             }
#         """)
#         recover_button.clicked.connect(self.recover)
#         layout.addWidget(recover_button)

#         login_button = QPushButton("Volver al inicio de sesión")
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

#         layout.addStretch()

#         self.setLayout(layout)

#     def recover(self):
#         email = self.email_input.text()

#         if not email:
#             self.show_error("Por favor, ingrese su correo electrónico.")
#             return

#         if not self.validate_email(email):
#             self.show_error("Por favor, ingrese un correo electrónico válido.")
#             return

#         QMessageBox.information(self, "Éxito", "Se han enviado las instrucciones de recuperación a su correo electrónico.")

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
#     recover_screen = RecoverScreen()
#     recover_screen.show()
#     sys.exit(app.exec_())





from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from screens.auth.styles.styles import get_screen_styles, get_main_button_styles, get_additional_buttons_styles

class RecoverScreen(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(get_screen_styles())

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title_label = QLabel("Recuperar Contraseña")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(title_label)

        instruction_label = QLabel("Ingresa tu correo electrónico y te enviaremos instrucciones para restablecer tu contraseña.")
        instruction_label.setWordWrap(True)
        instruction_label.setStyleSheet("font-size: 14px; color: #555; margin-bottom: 10px;")
        instruction_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(instruction_label)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Correo electrónico")
        layout.addWidget(self.email_input)

        recover_button = QPushButton("Enviar instrucciones")
        recover_button.setStyleSheet(get_main_button_styles())
        # recover_button.clicked.connect(self.recover)
        layout.addWidget(recover_button)

        self.login_button = QPushButton("Volver al inicio de sesión")
        self.login_button.setStyleSheet(get_additional_buttons_styles())
        layout.addWidget(self.login_button)

        layout.addStretch()

        self.setLayout(layout)