from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QCloseEvent
import typing
import Application.Notifier as Notifier
import sys
app = QApplication([])
if 'twisted.internet.reactor' in sys.modules:
    del sys.modules['twisted.internet.reactor']
import qt5reactor
qt5reactor.install()
from twisted.internet import reactor

class myMainWindow(QMainWindow):
    def closeEvent(self, event: QCloseEvent) -> None:
        print('closing from event!')
        if notifier.scrapTask.running:
            notifier.scrapTask.stop()
        QCoreApplication.instance().quit()

if __name__=="__main__":    
    window = myMainWindow()
    notifier = Notifier.Ui_mainWindow()

    notifier.setupUi(window)
    window.show()
    reactor.run()
    sys.exit()

