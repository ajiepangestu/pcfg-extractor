import PyQt5.QtCore as qtcore
import PyQt5.QtWidgets as qtwidget
import PyQt5.QtWebEngineWidgets as qtwebenginewidget

from threading import Thread

class GUI(object):
    def __init__(self, app, host="127.0.0.1", port=5000, debug=False):
        self.flask = app
        self.host = host
        self.port = port
        self.debug = debug

        self.app = qtwidget.QApplication([])
        self.view = qtwebenginewidget.QWebEngineView(self.app.activeModalWidget())
        self.view.setWindowTitle("PCFG Extractor")
        self.view.setFixedSize(500,500)

    def run(self):
        # Run Flask
        self.flask_thread = Thread(target=self.run_flask,args=(self.host, self.port, self.debug))
        self.flask_thread.daemon = True
        self.flask_thread.start()

        # Run Qt
        self.view.load(qtcore.QUrl("http://{}:{}".format(self.host, self.port)))
        self.view.show()
        self.app.exec_()

    def run_flask(self, host, port, debug):
        self.flask.run(host=host, port=port, debug=debug, use_reloader=False)