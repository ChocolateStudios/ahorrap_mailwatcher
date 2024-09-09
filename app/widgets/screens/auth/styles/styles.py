def get_screen_styles():
    return """
        QWidget {
            background-color: #f0f0f0;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        QLineEdit {
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: white;
            font-size: 14px;
        }
        QPushButton {
            padding: 12px;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
        }
    """


def get_main_button_styles():
    return """
        QPushButton {
            background-color: #4CAF50;
            color: white;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
    """
    

def get_additional_buttons_styles():
    return """
        QPushButton {
            background-color: transparent;
            color: #4CAF50;
            font-weight: normal;
            text-align: left;
            padding: 5px 0;
        }
        QPushButton:hover {
            text-decoration: underline;
        }
    """