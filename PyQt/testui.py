from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        #Mainwindow
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(800,600)

        # create stacked widget for the different pages
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        # create layout of two pages
        layout1 = QGridLayout()
        layout2 = QVBoxLayout()
        
        # create page 
        page1 = QWidget()
        page2 = QWidget()

        #pull image button
        self.pushButton1 = QPushButton("Pull Image")
        #self.pushButton1.setGeometry(QtCore.QRect(60, 50, 250, 90))
        self.pushButton1.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")

        #run container button
        self.pushButton2 = QtWidgets.QPushButton("Run Container")
        #self.pushButton2.setGeometry(QtCore.QRect(490, 50, 250, 90))
        self.pushButton2.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")

        #get data button
        self.pushButton3 = QtWidgets.QPushButton("Get Data")
        #self.pushButton3.setGeometry(QtCore.QRect(60, 180, 250, 90))
        self.pushButton3.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")

        #visualize button
        self.pushButton4 = QtWidgets.QPushButton("Visualize")
        #self.pushButton4.setGeometry(QtCore.QRect(490, 180, 250, 90))
        self.pushButton4.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")

        #SQL button
        self.pushButton5 = QtWidgets.QPushButton("SQL")
        #self.pushButton5.setGeometry(QtCore.QRect(60, 310, 250, 90))
        self.pushButton5.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        
        #Manage data button
        self.pushButton6 = QtWidgets.QPushButton("Manage Data")
        #self.pushButton6.setGeometry(QtCore.QRect(490, 310, 250, 90))
        self.pushButton6.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")

        #stop containers button
        self.pushButton7 = QtWidgets.QPushButton("Stop Containers")
        #self.pushButton7.setGeometry(QtCore.QRect(490, 440, 250, 90))
        self.pushButton7.setFixedSize(250, 90)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton7")


        layout1.addWidget(self.pushButton1, 0, 0) # Add the button to the grid layout1 at row 0, column 0
        layout1.addWidget(self.pushButton2, 0, 1) # Add the button to the grid layout1 at row 0, column 1
        layout1.addWidget(self.pushButton3, 0, 2) # Add the button to the grid layout1 at row 0, column 2
        layout1.addWidget(self.pushButton4, 1, 0) # Add the button to the grid layout1 at row 1, column 0
        layout1.addWidget(self.pushButton5, 1, 1) # Add the button to the grid layout1 at row 1, column 1
        layout1.addWidget(self.pushButton6, 1, 2) # Add the button to the grid layout1 at row 1, column 2
        layout1.addWidget(self.pushButton7, 3, 0) # Add the button to the grid layout1 at row 3, column 0

        #add layout1 to page1
        page1.setLayout(layout1)
        

        #configure 2nd page
        layout2.addWidget(QLabel("This is page 2"))
        button2 = QPushButton("Go to page 1")
        layout2.addWidget(button2)
        page2.setLayout(layout2)

        # add pages to the main stacked widget
        self.stackedWidget.addWidget(page1)
        self.stackedWidget.addWidget(page2)

        # add button functionality for page 1
        #self.pushButton1.clicked.connect(self.openNewWindow)
        self.pushButton2.clicked.connect(self.runCommand)
        self.pushButton3.clicked.connect(self.getData)
        self.pushButton4.clicked.connect(self.open_browser)
        self.pushButton5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(page2))
        self.pushButton6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(page2))
        self.pushButton7.clicked.connect(self.stopCommand)
        


        #buttons for page 2
        button2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(page1))

    def open_browser(self):
        url = "http://localhost:8501"
        QDesktopServices.openUrl(QUrl(url))

    def runCommand(self):
        process = QProcess(None)
        command1 = r'docker-compose -f C:\Users\Owner\Desktop\FYP\Changes\FypApp\docker-compose.yml up'
        process.start(command1)
        process.waitForFinished()
        output = process.readAllStandardOutput().data().decode()
        print(output)

    def stopCommand(self):
        process = QProcess(None)
        command = r'docker-compose -f C:\Users\Owner\Desktop\FYP\Changes\FypApp\docker-compose.yml down'
        process.start(command)
        process.waitForFinished()
        output = process.readAllStandardOutput().data().decode()
        print(output)

    #for now its just to take data from volume to viscontainer
    def getData(self):
        process = QProcess(None)
        command = r'docker cp C:\Users\Owner\Desktop\FYP\Changes\hadoop_namenode\output viscontainer:/usr/local/'
        process.start(command)
        process.waitForFinished()
        output = process.readAllStandardOutput().data().decode()
        print(output)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

