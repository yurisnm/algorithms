import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class GraphicsView(QGraphicsView):

    def __init__(self):
        super(GraphicsView, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setScene(GraphicsScene())

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())

    def resizeEvent(self, QResizeEvent):
        self.setSceneRect(QRectF(self.viewport().rect()))

class GraphicsScene(QGraphicsScene):

    def __init__(self):
        super(GraphicsScene, self).__init__()
        self.init_ui()

    def init_ui(self):
        pass

    def resizeEvent(self, QResizeEvent):
        self.setSceneRect(QRectF(self.viewport().rect()))


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.gv = GraphicsView()
        self.central_widget = QWidget()
        self.central_widget.setFixedSize(150,200)
        self.central_widget.setLayout(self.layout)
        self.layout.addWidget(self.gv)
        self.setCentralWidget(self.central_widget)
        self.setFixedSize(150,200)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    print("Size is (150, 200)")
    print("Putting in (50, 125) - This point should return (50.0, 75.0)")
    p0 = QPoint(50, 125)
    print("Before show():", mw.gv.mapToScene(p0))
    mw.show()
    mw.close()
    print("After show() :", mw.gv.mapToScene(p0))

    sys.exit(app.exec_())