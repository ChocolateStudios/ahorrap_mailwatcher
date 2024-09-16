def get_screen_styles():
    return """
        QWidget {
            background-color: #f0f0f0;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        QPushButton {
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
        }
        QPushButton#syncButton {
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            font-size: 14px;
        }
        QPushButton#syncButton:hover {
            background-color: #45a049;
        }
        QPushButton#iconButton {
            background-color: transparent;
            padding: 10px;
        }
        QPushButton#iconButton:hover {
            background-color: rgba(0, 0, 0, 0.1);
        }
    """