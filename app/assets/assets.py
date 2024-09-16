from PyQt5.QtGui import QIcon
import os

# auxiliar methods
current_dir = os.path.dirname(os.path.abspath(__file__))

def get_icon_path(relative_path):
    return os.path.join(current_dir, relative_path)


# RESOURCES

app_icon = get_icon_path("./images/AhorrAppIcon.png")
gear_icon = get_icon_path("./images/gear.png")
logout_icon = get_icon_path("./images/logout.png")