from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QTimer, QPoint

class LoadingButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.loading = False
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)

    def update_angle(self):
        self.angle = (self.angle + 10) % 360
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.loading:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255))
            
            size = min(self.width(), self.height()) // 3
            center = QPoint(self.width() - size - 10, self.height() // 2)
            painter.translate(center)
            painter.rotate(self.angle)

            thickness = size // 5
            for i in range(8):
                painter.rotate(45)
                painter.drawEllipse(-thickness, -size//2, thickness * 2, size//5)

    def start_loading(self):
        self.loading = True
        self.timer.start(50)

    def stop_loading(self):
        self.loading = False
        self.timer.stop()
        self.update()