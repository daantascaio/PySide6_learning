# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget

app = QApplication(sys.argv)

button = QPushButton('Texto do Botão')
button.setStyleSheet('font-size: 80px')
button.show()  # Adicionar o widget na hierarquia e exibe a janela

button2 = QPushButton('Texto do botão 2')
button2.setStyleSheet('font-size: 40px; background: red;')
button2.show()

central_widget = QWidget()

app.exec()  # Loop da aplicação
