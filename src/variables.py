from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'


# Sizing
BIG_FONT_SIZE = 30
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 16
HEIGHT_TEXT_SIZE = int(BIG_FONT_SIZE + (BIG_FONT_SIZE / 3))
TEXT_MARGIN = 5
MINIMUM_WIDTH = 500
