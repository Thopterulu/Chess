# chess is 8 by 8 so let's do a 8 by 8 board

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
class Window(QMainWindow):
   def __init__(self):
       super().__init__()
 
       self.setGeometry(300, 300, 800, 600)
       self.setWindowTitle("Chess")
       self.show()
       self.activateWindow()
 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())