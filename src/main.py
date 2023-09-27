import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLineEdit
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons_ import Button, ButtonsGrid

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    print(icon)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText('Write thing')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
