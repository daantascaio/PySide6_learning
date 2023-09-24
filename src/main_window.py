from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
