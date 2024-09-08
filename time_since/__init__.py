import os

HERE = os.path.dirname(__file__)
ICONS_DIR = os.path.join(HERE, "icons")
ICONS = [os.path.join(ICONS_DIR, f) for f in os.listdir(ICONS_DIR)]
