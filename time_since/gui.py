import sys
import time
import datetime

from PyQt5.QtWidgets import (
   QApplication, QWidget, QSystemTrayIcon,
   QLabel, QAction, QMenu,
   QHBoxLayout
)
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QThread, pyqtSignal

from time_since.util import read_time, calculate_delta, Delta
from time_since import ICONS

class DeltaDialog(QWidget):
   """Widget to display time delta when tray icon is right-clicked"""
   def __init__(self, start: datetime.datetime):
      super().__init__()
      self.setWindowTitle("Elapsed Time")
      layout = QHBoxLayout()
      self.delta = calculate_delta(start)
      self.deltaThread = DeltaThread(start)
      self.deltaThread.update.connect(self.updateDelta)
      self.deltaThread.start()
      self.message = QLabel()
      layout.addWidget(self.message)
      self.setLayout(layout)
   
   def updateDelta(self, delta):
      self.delta = delta
      self.message.setText(str(self.delta))

class DeltaThread(QThread):
    """Thread which maintains the loop that calculates the delta for the gui"""
    update = pyqtSignal(Delta)
    def __init__(self, t0: datetime.datetime, frequency: int = 1):
        super().__init__()
        self.t0 = t0
        self.frequency = frequency
    def run(self):
        while True:
            self.update.emit(calculate_delta(self.t0))
            time.sleep(self.frequency)

class DeltaTrayIcon(QSystemTrayIcon):
   """Tray icon to allow interaction with app"""
   def __init__(self, dialog, icon, app):
      super().__init__()
      self.dialog = dialog
      self.setIcon(icon)
      self.setVisible(True)
      menu = QMenu()
      # Have to create a reference to any QActions attached to the QMenu here.
      # If not, the context menu returned by contextMenu() for some reason does
      # not keep references to them, and presumably they are garbage-collected.
      # Thus, any calls to popup() would show nothing b/c there are no actions.
      self.quitAction = QAction("Quit")
      self.quitAction.triggered.connect(app.quit)
      menu.addAction(self.quitAction)
      self.activated.connect(self.onActivated)
      self.setContextMenu(menu)
   
   def onActivated(self, reason):
      if reason == self.ActivationReason.Trigger:
         self.dialog.show()
      elif reason == self.ActivationReason.Context:
         self.contextMenu().popup(QCursor.pos())

def run():
   app = QApplication([]) 
   app.setQuitOnLastWindowClosed(False)
   icon = QIcon(ICONS[0])
   dialog = DeltaDialog(read_time())
   tray = DeltaTrayIcon(dialog, icon, app)
   tray.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   run()