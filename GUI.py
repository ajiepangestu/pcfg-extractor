import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtWebEngineWidgets as QtWebEngineWidgets
from threading import Thread

class GUI:
    def __init__(self, app, host="127.0.0.1", port=5000, debug=False):
        self.flask = app
        self.host = host
        self.port = port
        self.debug = debug

        self.app = QtWidgets.QApplication([])
        self.view = QtWebEngineWidgets.QWebEngineView(self.app.activeModalWidget())
        self.view.setWindowTitle("PCFG Extractor")
        self.view.setFixedSize(1300,500)

    def run(self):
        # Run Flask
        self.flask_thread = Thread(target=self.flask.run,args=(self.host, self.port, self.debug))
        self.flask_thread.daemon = True
        self.flask_thread.start()

        # Run Qt
        self.view.load(QtCore.QUrl("http://{}:{}".format(self.host, self.port)))
        self.view.show()
        self.app.exec_()
