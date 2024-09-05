from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from qtawesome import icon
from screens.main.styles.styles import get_styles

class HomeScreen(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(get_styles())

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Top bar with settings button
        top_bar = QHBoxLayout()
        self.settings_button = QPushButton(icon('fa5s.cog'), "")
        self.settings_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 24px;
                color: #4CAF50;
            }
            QPushButton:hover {
                color: #45a049;
            }
        """)
        top_bar.addStretch()
        top_bar.addWidget(self.settings_button)

        main_layout.addLayout(top_bar)

        # Spacer to push content to the center
        main_layout.addStretch()

        # Sync button
        self.sync_button = QPushButton("Sincronizar")
        self.sync_button.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.sync_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 25px;
                padding: 20px 40px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        main_layout.addWidget(self.sync_button, alignment=Qt.AlignCenter)

        # Spacer to push content to the center
        main_layout.addStretch()

        # Bottom bar with logout button
        bottom_bar = QHBoxLayout()
        self.logout_button = QPushButton(icon('fa5s.sign-out-alt'), "")
        self.logout_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 24px;
                color: #FF5722;
            }
            QPushButton:hover {
                color: #E64A19;
            }
        """)
        bottom_bar.addWidget(self.logout_button)
        bottom_bar.addStretch()

        main_layout.addLayout(bottom_bar)

        self.setLayout(main_layout)