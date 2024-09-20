import asyncio
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from qasync import asyncSlot

from app.core.expenses.usecases.synchronize_expenses_usecase import SynchronizeExpensesUseCase
from app.core.users.usecases.logout_user_usecase import LogoutUserUseCase
from app.widgets.screens.main.styles.styles import get_screen_styles
from app.assets.assets import gear_icon, logout_icon

class HomeScreen(QFrame):
    def __init__(self, app_manager):
        super().__init__()
        self.initUI()
        
        self.app_manager = app_manager
        self.synchronize_expenses_usecase = SynchronizeExpensesUseCase()
        self.logout_user_usecase = LogoutUserUseCase(self.app_manager.local_storage)

    def initUI(self):
        self.setStyleSheet(get_screen_styles())

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Título
        title_label = QLabel("AhorrApp'e")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-bottom: 20px;")
        main_layout.addWidget(title_label)

        # Botón de sincronización
        sync_button = QPushButton("Sincronizar")
        sync_button.setObjectName("syncButton")
        sync_button.clicked.connect(self.sync_data)
        main_layout.addStretch(1)
        main_layout.addWidget(sync_button, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)

        # Botones de ajustes y cerrar sesión
        bottom_layout = QHBoxLayout()
        
        settings_button = QPushButton()
        settings_button.setIcon(QIcon(gear_icon))
        settings_button.setObjectName("iconButton")
        settings_button.setToolTip("Ajustes")
        settings_button.clicked.connect(self.open_settings)
        
        logout_button = QPushButton()
        logout_button.setIcon(QIcon(logout_icon))
        logout_button.setObjectName("iconButton")
        logout_button.setToolTip("Cerrar sesión")
        logout_button.clicked.connect(self.logout)

        bottom_layout.addWidget(settings_button)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(logout_button)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    @asyncSlot()
    async def sync_data(self):
        print("Sincronizando datos...")
        # await self.synchronize_expenses_usecase.synchronize_expenses()
        
        asyncio.create_task(self.synchronize_expenses_usecase.synchronize_expenses())

    def open_settings(self):
        print("Abriendo ajustes...")
        # Aquí iría la lógica para abrir la pantalla de ajustes

    def logout(self):
        print("Cerrando sesión...")
        # Aquí iría la lógica para cerrar sesión
        self.logout_user_usecase.logout_user()
        self.app_manager.central_widget.setCurrentWidget(self.app_manager.login_screen)

