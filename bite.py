from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QPushButton, QVBoxLayout,
                             QWidget, QLabel, QTableWidget, QTableWidgetItem)


class PyBite(QWidget):
    def __init__(self):
        super().__init__()
        self.createLeftGroupBox()
        self.createRightGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.LeftGroupBox, 1, 0)
        mainLayout.addWidget(self.RightGroupBox, 1, 1, 1, 3)
        self.setLayout(mainLayout)

    def createLeftGroupBox(self):
        self.LeftGroupBox = QGroupBox("Group 1")
        self.LeftGroupBox.setStyleSheet("background-color:#a41d1d; color: #ffffff;")

        introText = QLabel("Happy Coding,Ninja!")
        introText.setStyleSheet(
            """
        QLabel {
            text-align: center;
            font-size: 28px;
            background: transparent;
            margin: 20px 0px;
        }
        """
        )

        logo = QLabel(self)
        pixmap = QPixmap("assets/images/logo.png")
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        # Optional, resize window to image size
        self.resize(pixmap.width(), pixmap.height())

        dashBoardButton = QPushButton("Dashboard")
        dashBoardButton.setCheckable(True)

        bitesOfPyButton = QPushButton("Bites of Py")
        bitesOfPyButton.setCheckable(True)

        blogChallengesButton = QPushButton("Blog Challenges")
        blogChallengesButton.setCheckable(True)

        hundredDaysButton = QPushButton("100DaysOfCode")
        hundredDaysButton.setCheckable(True)

        messagesButton = QPushButton("Messages")
        messagesButton.setCheckable(True)

        settingsButton = QPushButton("Messages")
        settingsButton.setCheckable(True)

        pyBitesBlogButton = QPushButton("PyBites Blog")
        pyBitesBlogButton.setCheckable(True)

        layout = QVBoxLayout()
        layout.addWidget(logo)
        layout.addWidget(introText)
        layout.addWidget(dashBoardButton)
        layout.addWidget(bitesOfPyButton)
        layout.addWidget(blogChallengesButton)
        layout.addWidget(hundredDaysButton)
        layout.addWidget(messagesButton)
        layout.addWidget(settingsButton)
        layout.addWidget(pyBitesBlogButton)
        layout.addStretch(1)

        self.LeftGroupBox.setLayout(layout)

    def createRightGroupBox(self):
        self.RightGroupBox = QGroupBox("Group 2")
        self.RightGroupBox.setStyleSheet("background-color:#ffffff; color: #000000;")
        self.createTable()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.setStretch(0, 1)
        self.RightGroupBox.setLayout(layout)


    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(40)
        self.tableWidget.setColumnCount(20)
        self.tableWidget.move(0, 0)
        self.tableWidget.showMaximized()
