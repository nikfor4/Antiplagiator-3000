
from PyQt5.QtWidgets import QApplication, QMainWindow





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
