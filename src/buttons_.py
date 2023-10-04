from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: "Display", info: "Info", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):

                if buttonText == "":
                    continue

                if not buttonText == '0':

                    button = Button(buttonText)

                    if not isNumOrDot(buttonText):
                        button.setProperty("cssClass", "specialButton")
                        self._configSpecialButton(button)

                    self.addWidget(button, i, j)

                    slot = self._makeSlot(
                        self._insertButtonTextToDisplay, button
                    )
                    self._connectButtonClicked(button, slot)

                else:
                    button0 = Button(buttonText)
                    self.addWidget(button0, i, j-1, 1, 2,)

                    buttonSlot0 = self._makeSlot(
                        self._insertButtonTextToDisplay, button0
                    )

                    button0.clicked.connect(buttonSlot0)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        buttonText = button.text()

        if buttonText == 'C':
            slot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, slot)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self.display.clear()
