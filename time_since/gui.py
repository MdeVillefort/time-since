import sys
import time

from PyQt5.QtWidgets import (
   QApplication, QWidget, QSystemTrayIcon,
   QLabel, QAction, QMenu
)
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QPoint

from time_since.util import read_time, calculate_delta
from time_since import ICONS

class DeltaDisplay(QWidget):
   """Widget to display time delta when tray icon is right-clicked"""
   def __init__(self):
      super().__init__()
      self.setGeometry(100, 100, 280, 80)
      self.message = QLabel(self)
      self.message.setText("Hello, World!")
      self.message.move(110, 40)

class ApplicationTrayIcon(QSystemTrayIcon):
   """Tray icon to allow interaction with app"""
   def __init__(self, widget, icon, app):
      super().__init__()
      self.widget = widget
      self.setIcon(icon)
      self.setVisible(True)
      menu = QMenu()
      menu.addAction(QAction("TEST1"))
      menu.addAction(QAction("TEST2"))
      quit = QAction("Quit")
      quit.triggered.connect(app.quit)
      menu.addAction(quit)
      self.activated.connect(self.onActivated)
      self.setContextMenu(menu)
   
   def onActivated(self, reason):
      if reason == self.ActivationReason.Trigger:
         self.widget.show()
      elif reason == self.ActivationReason.Context:
         self.contextMenu().popup(QCursor.pos()) # This does not work!? WHY!!??

def run():
   app = QApplication([]) 
   app.setQuitOnLastWindowClosed(False)
   icon = QIcon(ICONS[0])
   display = DeltaDisplay()
   tray = ApplicationTrayIcon(display, icon, app)
   tray.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   run()