import sys
import first
import MainWinForm
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    mainWindow = QMainWindow()

    ui = MainWinForm.Ui_MainWindow()

    # 向主窗体添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())




