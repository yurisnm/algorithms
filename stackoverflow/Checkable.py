'''An example file with a QAction that stays checkable.'''

# IMPORT STANDARD LIBRARIES
import sys

# IMPORT THIRD-PARTY LIBRARIES
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidgetAction



class CheckBox(QCheckBox):

    def __init__(self, name):
        super(CheckBox, self).__init__()
        self.update_color()
        self.setText(name)

    def mousePressEvent(self, event):
        self.update_color()
        super(CheckBox, self).mousePressEvent(event)


    def update_color(self):
        if self.isChecked():
            print("unchecked")
            self.setStyleSheet("color: gray;")
        else:
            print("checked")
            self.setStyleSheet("")

class Menu(QMenu):

    def __init__(self, text):
        super(Menu, self).__init__()
        self.setTitle(text)
        self.setStyleSheet("""
                QMenu:tearoff{
                    background-color: green;
                    color: red;
                    border: 10px
                    solid yellow;
                }
                """)




class WindowTest(QWidget):

    '''A basic window.'''

    def __init__(self, parent=None):
        '''Init the window.'''
        super(WindowTest, self).__init__(parent=parent)
        self.setLayout(QHBoxLayout())
        self.menubar = QMenuBar(parent=self)
        self.menu = Menu("Some Menu")
        self.ac = QAction("act")
        self.ac.setCheckable(True)

        self.menubar.addMenu(self.menu)
        self.menu.setContentsMargins(10,10,10,10)

        self.widget_action = QWidgetAction(self)
        self.button = CheckBox("some")
        self.button.setCheckable(True)
        self.button.setFixedSize(100, 20)
        self.widget_action.setDefaultWidget(self.button)
        self.menu.addAction(self.widget_action)
        self.menu.addAction(self.ac)

        self.menu.setTearOffEnabled(True)

        self.setWindowModality(Qt.WindowModal)


        self.setFixedSize(500,200)


def main():
    '''Do the window test.'''
    qapp = QApplication(sys.argv)
    window = WindowTest()
    window.show()
    sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()