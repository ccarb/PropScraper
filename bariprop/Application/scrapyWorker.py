from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class ScrapyWorker(QtCore.QObject):
    logChanged = QtCore.pyqtSignal(str)
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ScrapyWorker, self).__init__(parent)
        self._process = QtCore.QProcess(self)
        self._process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self._process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self._process.setProgram('scrapy')
        self._process.started.connect(self.started)
        self._process.finished.connect(self.finished)
        self.logChanged.connect(self.insert_log)

    def run(self, project, spider):
        self._process.setWorkingDirectory(project)
        self._process.setArguments(['crawl', spider])
        self._process.start()

    def runAllSpiders(self,project):
        self._process.setWorkingDirectory(project)
        spiders=self.spiders(project)
        for spider in spiders:
            loop = QtCore.QEventLoop()
            self._process.finished.connect(loop.quit)
            self._process.setArguments(['crawl', spider])
            self._process.start()
            loop.exec_()

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        data = self._process.readAllStandardOutput().data()
        data = str(data)
        self.logChanged.emit(data)

    @QtCore.pyqtSlot()
    def stop(self):
        self._process.kill()

    def spiders(self, project):
        process = QtCore.QProcess()
        process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        process.setWorkingDirectory(project)
        loop = QtCore.QEventLoop()
        process.finished.connect(loop.quit)
        process.start('scrapy', ['list'])
        loop.exec_()
        return process.readAllStandardOutput().data().decode().split()

    @QtCore.pyqtSlot(str)
    def insert_log(self, text):
        #prev_cursor = self.text_edit.textCursor()
        #self.text_edit.moveCursor(QtGui.QTextCursor.End)
        #self.text_edit.insertPlainText(text)
        #self.text_edit.setTextCursor(prev_cursor)
        print(text)
        