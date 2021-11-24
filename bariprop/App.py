from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon,QAction,QMenu
import Application.Notifier as Notifier
import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()

    notifier = Notifier.Ui_mainWindow()
    notifier.setupUi(window)
    window.show()
    app.exec()