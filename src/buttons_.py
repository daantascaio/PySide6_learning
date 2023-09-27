from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setCheckable(True)
        # self.setContentsMargins(0, 0, 0, 0)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):

                if buttonText == "":
                    continue

                if not buttonText == '0':

                    button = Button(buttonText)

                    if not isNumOrDot(buttonText):
                        button.setProperty("cssClass", "specialButton")

                    self.addWidget(button, i, j)

                    buttonSlot = self._makeButtonDisplaySlot(
                        self._insertButtonTextToDisplay, button
                    )
                    button.clicked.connect(buttonSlot)

                else:
                    button0 = Button(buttonText)
                    self.addWidget(button0, i, j-1, 1, 2,)

                    buttonSlot0 = self._makeButtonDisplaySlot(
                        self._insertButtonTextToDisplay, button0
                    )

                    button0.clicked.connect(buttonSlot0)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
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
