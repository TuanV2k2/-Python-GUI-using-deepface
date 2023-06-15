from PySide2 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import *
from database import DatabaseManager
import sys
import datetime
import cv2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 442)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 290, 410))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 410))
        self.label.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 260, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 180, 150))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0, 125, 236, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 365, 211, 16))
        self.label_3.setStyleSheet("color:rgba(255, 255, 255, 150);")
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent = lambda event: self.open_signup_form()
        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/4856718.png"), QIcon.Normal, QIcon.Off)  # Replace "/path/to/icon.png" with the path to the icon in the resource file
        Form.setWindowIcon(icon)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.mousePressEvent = lambda event: self.login()
        self.form = Form
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g   I n"))
        self.label_2.setText(_translate("Form", "Log In"))
        self.label_3.setText(_translate("Form", "Wanna sign up ?"))

    def open_signup_form(self):
        Form = QtWidgets.QDialog()
        ui = Ui_Form_signup()
        ui.setupUi(Form)
        Form.exec_()

    def login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()

        database = DatabaseManager()
        result = database.find_account(name, password)
        cap=cv2.VideoCapture(0)  
        face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if (result != None):
            while True:
                ret, frame = cap.read()
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
                for (x, y, w, h) in faces_detected:
                    cv2.rectangle(frame, (x-10, y-25), (x + w + 10, y + h + 25), (255, 0, 0), thickness=7)
                    face_pic = frame[y-25:y+h+25, x-10:x+w+10]
                    if cv2.waitKey(1) == ord("a"):
                        cv2.imwrite("customer.jpg" , face_pic)
                        with open('customer.jpg', 'rb') as f:
                            image_data = f.read()
                        database = DatabaseManager()
                        current_time = datetime.datetime.now()
                        month = current_time.month 
                        day = current_time.day
                        year = current_time.year
                        database.insert_employee_login(result,day, month, year, image_data)
                        self.form.close()
                        from main import MainWindow
                        window = MainWindow()
                        cap.release()
                        return cv2.destroyAllWindows()
                        
                resized_img = cv2.resize(frame, (1000, 700))
                cv2.imshow('Camera', resized_img)

            


class Ui_Form_signup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 442)
        #Form.setWindowFlags(QtCore.Qt.FramelesswindowHint)
        #QtCore.Qt.FramelesswindowHint
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 290, 410))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 410))
        self.label.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 260, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 180, 150))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0, 125, 236, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2") 
        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/4856718.png"), QIcon.Normal, QIcon.Off)  # Replace "/path/to/icon.png" with the path to the icon in the resource file
        Form.setWindowIcon(icon)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.mousePressEvent = lambda event: self.signup()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "S i g n   U p"))
        self.label_2.setText(_translate("Form", "Sign Up"))

    def signup(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()

        cap=cv2.VideoCapture(0)  
        face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
          ret, frame = cap.read()
          gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
          for (x, y, w, h) in faces_detected:
              cv2.rectangle(frame, (x-10, y-25), (x + w + 10, y + h + 25), (255, 0, 0), thickness=7)
              face_pic = frame[y-25:y+h+25, x-10:x+w+10]
              if cv2.waitKey(1) == ord("a"):
                    cv2.imwrite("customer.jpg" , face_pic)
                    with open('customer.jpg', 'rb') as f:
                        image_data = f.read()
                    database = DatabaseManager()
                    database.insert_employee(name, password, image_data)
                    cap.release()
                    return cv2.destroyAllWindows() 
          resized_img = cv2.resize(frame, (1000, 700))
          cv2.imshow('Camera', resized_img)


        

