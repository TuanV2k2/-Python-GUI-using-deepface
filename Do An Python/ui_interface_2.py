# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 512)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"#LeftMenuSubContainer{\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#LeftMenuSubContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"#CenterMenuSubContainer, #rightSubMenuContainer{\n"
"    background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_4, #frame_8, #popupNotificationSubContainer{\n"
"    background-color: #16191d;\n"
"    border-radius: 10px\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"   background-color: #2c313c;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftMenuContainer = QCustomSlideMenu(parent=self.centralwidget)
        self.LeftMenuContainer.setMaximumSize(QtCore.QSize(50, 16777215))
        self.LeftMenuContainer.setObjectName("LeftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LeftMenuSubContainer = QtWidgets.QWidget(parent=self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName("LeftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.LeftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBtn.sizePolicy().hasHeightForWidth())
        self.menuBtn.setSizePolicy(sizePolicy)
        self.menuBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.LeftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.homeBtn = QtWidgets.QPushButton(parent=self.frame_2)
        self.homeBtn.setStyleSheet("background-color: #1f232a;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/home-button (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_4.addWidget(self.homeBtn)
        self.dataAnalysysBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/analysis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.dataAnalysysBtn.setIcon(icon2)
        self.dataAnalysysBtn.setIconSize(QtCore.QSize(24, 24))
        self.dataAnalysysBtn.setObjectName("dataAnalysysBtn")
        self.verticalLayout_4.addWidget(self.dataAnalysysBtn)
        self.reportsBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/chart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.reportsBtn.setIcon(icon3)
        self.reportsBtn.setIconSize(QtCore.QSize(24, 24))
        self.reportsBtn.setObjectName("reportsBtn")
        self.verticalLayout_4.addWidget(self.reportsBtn)
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(parent=self.LeftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.settingBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingBtn.setObjectName("settingBtn")
        self.verticalLayout_5.addWidget(self.settingBtn)
        self.InfoBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/information.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.InfoBtn.setIcon(icon5)
        self.InfoBtn.setIconSize(QtCore.QSize(24, 24))
        self.InfoBtn.setObjectName("InfoBtn")
        self.verticalLayout_5.addWidget(self.InfoBtn)
        self.helpBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/question-mark.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QtCore.QSize(24, 24))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_5.addWidget(self.helpBtn)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.LeftMenuSubContainer)
        self.horizontalLayout.addWidget(self.LeftMenuContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.CenterMenuContainer = QCustomSlideMenu(parent=self.centralwidget)
        self.CenterMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.CenterMenuContainer.setObjectName("CenterMenuContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.CenterMenuContainer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CenterMenuSubContainer = QtWidgets.QWidget(parent=self.CenterMenuContainer)
        self.CenterMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.CenterMenuSubContainer.setObjectName("CenterMenuSubContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.CenterMenuSubContainer)
        self.verticalLayout_6.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(parent=self.CenterMenuSubContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.closeCenterMenuBtn = QtWidgets.QPushButton(parent=self.frame_4)
        self.closeCenterMenuBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeCenterMenuBtn.setObjectName("closeCenterMenuBtn")
        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.CenterMenuSubContainer)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.CenterMenuSubContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.CenterMenuContainer)
        self.MainBodyContainer = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy)
        self.MainBodyContainer.setStyleSheet("")
        self.MainBodyContainer.setObjectName("MainBodyContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.headerContainer = QtWidgets.QWidget(parent=self.MainBodyContainer)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_6 = QtWidgets.QFrame(parent=self.headerContainer)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/4856718.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(parent=self.headerContainer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.notificationBtn = QtWidgets.QPushButton(parent=self.frame_5)
        self.notificationBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/ring-bell.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QtCore.QSize(27, 27))
        self.notificationBtn.setObjectName("notificationBtn")
        self.horizontalLayout_6.addWidget(self.notificationBtn)
        self.moreMenuBtn = QtWidgets.QPushButton(parent=self.frame_5)
        self.moreMenuBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/ellipsis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.moreMenuBtn.setObjectName("moreMenuBtn")
        self.horizontalLayout_6.addWidget(self.moreMenuBtn)
        self.profileMenuBtn = QtWidgets.QPushButton(parent=self.frame_5)
        self.profileMenuBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.profileMenuBtn.setIcon(icon10)
        self.profileMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.profileMenuBtn.setObjectName("profileMenuBtn")
        self.horizontalLayout_6.addWidget(self.profileMenuBtn)
        self.horizontalLayout_5.addWidget(self.frame_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(parent=self.headerContainer)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimizeBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.minimizeBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_4.addWidget(self.minimizeBtn)
        self.restoreBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.restoreBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/square.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setIconSize(QtCore.QSize(20, 20))
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_4.addWidget(self.restoreBtn)
        self.closeBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.closeBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeBtn.setIcon(icon13)
        self.closeBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_4.addWidget(self.closeBtn)
        self.horizontalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_9.addWidget(self.headerContainer, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.mainBodyContainer = QtWidgets.QWidget(parent=self.MainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setMinimumSize(QtCore.QSize(579, 327))
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainBodyContainer)
        self.horizontalLayout_8.setContentsMargins(9, 1, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mainContentsContainers = QtWidgets.QWidget(parent=self.mainBodyContainer)
        self.mainContentsContainers.setObjectName("mainContentsContainers")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.mainContentsContainers)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(parent=self.mainContentsContainers)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setEnabled(True)
        self.page_6.setObjectName("page_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.picture = QtWidgets.QLabel(parent=self.page_6)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.verticalLayout_16.addWidget(self.picture)
        self.name = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout_16.addWidget(self.name)
        self.gender = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.verticalLayout_16.addWidget(self.gender)
        self.age = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.verticalLayout_16.addWidget(self.age)
        self.race = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.race.setFont(font)
        self.race.setObjectName("race")
        self.verticalLayout_16.addWidget(self.race)
        self.chocolate = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chocolate.setFont(font)
        self.chocolate.setObjectName("chocolate")
        self.verticalLayout_16.addWidget(self.chocolate)
        self.cafe = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cafe.setFont(font)
        self.cafe.setObjectName("cafe")
        self.verticalLayout_16.addWidget(self.cafe)
        self.latte = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.latte.setFont(font)
        self.latte.setLineWidth(1)
        self.latte.setObjectName("latte")
        self.verticalLayout_16.addWidget(self.latte)
        self.money = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.money.setFont(font)
        self.money.setObjectName("money")
        self.verticalLayout_16.addWidget(self.money)
        self.add_order = QtWidgets.QPushButton(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_order.setFont(font)
        self.add_order.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.add_order.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Whiteicons/whiteicons/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_order.setIcon(icon14)
        self.add_order.setIconSize(QtCore.QSize(50, 50))
        self.add_order.setObjectName("add_order")
        self.verticalLayout_16.addWidget(self.add_order)
        self.home = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.home.setFont(font)
        self.home.setText("")
        self.home.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.home.setObjectName("home")
        self.verticalLayout_16.addWidget(self.home)
        self.stackedWidget_3.addWidget(self.page_6)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setEnabled(True)
        self.page_8.setObjectName("page_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_12 = QtWidgets.QLabel(parent=self.page_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_18.addWidget(self.label_12)
        self.stackedWidget_3.addWidget(self.page_8)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setEnabled(True)
        self.page_7.setObjectName("page_7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.plot_1 = QtWidgets.QWidget(parent=self.page_7)
        self.plot_1.setObjectName("plot_1")
        self.verticalLayout_17.addWidget(self.plot_1)
        self.plot_2 = QtWidgets.QWidget(parent=self.page_7)
        self.plot_2.setObjectName("plot_2")
        self.verticalLayout_17.addWidget(self.plot_2)
        self.label_11 = QtWidgets.QLabel(parent=self.page_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_17.addWidget(self.label_11)
        self.stackedWidget_3.addWidget(self.page_7)
        self.verticalLayout_15.addWidget(self.stackedWidget_3)
        self.horizontalLayout_8.addWidget(self.mainContentsContainers)
        self.rightMenuContainer = QCustomSlideMenu(parent=self.mainBodyContainer)
        self.rightMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QtCore.QSize(200, 326))
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.rightSubMenuContainer = QtWidgets.QWidget(parent=self.rightMenuContainer)
        self.rightSubMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightSubMenuContainer.setObjectName("rightSubMenuContainer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.rightSubMenuContainer)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_8 = QtWidgets.QFrame(parent=self.rightSubMenuContainer)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.closeRightMenu = QtWidgets.QPushButton(parent=self.frame_8)
        self.closeRightMenu.setText("")
        self.closeRightMenu.setIcon(icon7)
        self.closeRightMenu.setIconSize(QtCore.QSize(24, 24))
        self.closeRightMenu.setObjectName("closeRightMenu")
        self.horizontalLayout_9.addWidget(self.closeRightMenu, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_11.addWidget(self.frame_8)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.rightSubMenuContainer)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(parent=self.page_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_9 = QtWidgets.QLabel(parent=self.page_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.stackedWidget_2.addWidget(self.page_5)
        self.verticalLayout_11.addWidget(self.stackedWidget_2)
        self.verticalLayout_10.addWidget(self.rightSubMenuContainer, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_8.addWidget(self.rightMenuContainer)
        self.verticalLayout_9.addWidget(self.mainBodyContainer)
        self.popupNotificationContainer = QCustomSlideMenu(parent=self.MainBodyContainer)
        self.popupNotificationContainer.setObjectName("popupNotificationContainer")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.popupNotificationSubContainer = QtWidgets.QWidget(parent=self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName("popupNotificationSubContainer")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_14 = QtWidgets.QLabel(parent=self.popupNotificationSubContainer)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_20.addWidget(self.label_14)
        self.frame_9 = QtWidgets.QFrame(parent=self.popupNotificationSubContainer)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.closeNotificationBtn = QtWidgets.QPushButton(parent=self.frame_9)
        self.closeNotificationBtn.setText("")
        self.closeNotificationBtn.setIcon(icon7)
        self.closeNotificationBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeNotificationBtn.setObjectName("closeNotificationBtn")
        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_20.addWidget(self.frame_9)
        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)
        self.verticalLayout_9.addWidget(self.popupNotificationContainer)
        self.footerContainer = QtWidgets.QWidget(parent=self.MainBodyContainer)
        self.footerContainer.setObjectName("footerContainer")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_11 = QtWidgets.QFrame(parent=self.footerContainer)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.horizontalLayout_11.addWidget(self.frame_11)
        self.sizeGrip = QtWidgets.QFrame(parent=self.footerContainer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(30, 30))
        self.sizeGrip.setMaximumSize(QtCore.QSize(30, 30))
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sizeGrip.setObjectName("sizeGrip")
        self.horizontalLayout_11.addWidget(self.sizeGrip)
        self.verticalLayout_9.addWidget(self.footerContainer)
        self.horizontalLayout.addWidget(self.MainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.dataAnalysysBtn.setToolTip(_translate("MainWindow", "Data Analysis"))
        self.dataAnalysysBtn.setText(_translate("MainWindow", "Data Analysis"))
        self.reportsBtn.setToolTip(_translate("MainWindow", "View reports"))
        self.reportsBtn.setText(_translate("MainWindow", "Reports"))
        self.settingBtn.setToolTip(_translate("MainWindow", "go to settings"))
        self.settingBtn.setText(_translate("MainWindow", "Settings"))
        self.InfoBtn.setToolTip(_translate("MainWindow", "Information about the app"))
        self.InfoBtn.setText(_translate("MainWindow", "Informations"))
        self.helpBtn.setToolTip(_translate("MainWindow", "Help"))
        self.helpBtn.setText(_translate("MainWindow", "Help"))
        self.label.setText(_translate("MainWindow", "More Menu"))
        self.closeCenterMenuBtn.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_2.setText(_translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "Informations"))
        self.label_4.setText(_translate("MainWindow", "Helps"))
        self.label_6.setText(_translate("MainWindow", "Coffee App"))
        self.moreMenuBtn.setToolTip(_translate("MainWindow", "More"))
        self.profileMenuBtn.setToolTip(_translate("MainWindow", "Profile"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Minimize Window"))
        self.restoreBtn.setToolTip(_translate("MainWindow", "Expand Window"))
        self.closeBtn.setToolTip(_translate("MainWindow", "Close Window"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.gender.setText(_translate("MainWindow", "Gender: "))
        self.age.setText(_translate("MainWindow", "Age:"))
        self.race.setText(_translate("MainWindow", "Race:"))
        self.chocolate.setText(_translate("MainWindow", "Chocolate"))
        self.cafe.setText(_translate("MainWindow", "Cafe"))
        self.latte.setText(_translate("MainWindow", "Latte:"))
        self.money.setText(_translate("MainWindow", "Money: "))
        self.label_12.setText(_translate("MainWindow", "Reports"))
        self.label_11.setText(_translate("MainWindow", "Data Analysis"))
        self.label_7.setText(_translate("MainWindow", "Right Menu"))
        self.closeRightMenu.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_8.setText(_translate("MainWindow", "Profiles"))
        self.label_9.setText(_translate("MainWindow", "More ..."))
        self.label_14.setText(_translate("MainWindow", "Notification"))
        self.label_13.setText(_translate("MainWindow", "Notification Message"))
        self.closeNotificationBtn.setToolTip(_translate("MainWindow", "close notification"))
        self.label_15.setText(_translate("MainWindow", "Copy Right V.T"))
from Custom_Widgets.Widgets import QCustomSlideMenu


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
