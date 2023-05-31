import cv2
import numpy as np
import imutils
from database import DatabaseManager
from PIL import Image
import io
import os
from deepface import DeepFace
from Custom_Widgets.Widgets import *
from PySide2 import *
import shutil
import datetime



# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.1.10:4747/video"
potential_images = []
"""
class registerForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(registerForm, self).__init__(parent)
        self.setWindowTitle("Register Form")
        self.resize(200, 200)
        
        layout = QtWidgets.QVBoxLayout(self)
        self.name_label = QtWidgets.QLabel("Name:")
        layout.addWidget(self.name_label)
        self.name_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.name_edit)
        self.enter_button = QtWidgets.QPushButton("Enter")
        layout.addWidget(self.enter_button)
        
        self.enter_button.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

"""
class ImageWindow(QDialog):
    def __init__(self, image_list, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Image window")
        self.resize(400, 400)

        layout = QVBoxLayout(self)
        # Create and add the image labels
        for image_file_path in image_list:
            image_label = QLabel(self)
            pixmap = QPixmap(image_file_path)
            image_label.setPixmap(pixmap)
            image_label.mousePressEvent = lambda event: self.image_handeler(image_file_path)
            layout.addWidget(image_label)

    def image_handeler(self, image_file_path):
        # Source file path
        source_file = image_file_path    
        image_file_name = os.path.basename(source_file)
        # Destination file path
        destination_file = "profile_image\\" + image_file_name

        #Copy the file
        shutil.copyfile(source_file, destination_file)

        self.close()
        



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 204)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 49, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 80, 75, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(130, 80, 75, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(230, 80, 75, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 120, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 170, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.handleButtonClicked(Dialog))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name: "))
        self.checkBox.setText(_translate("Dialog", "Chocolate"))
        self.checkBox_2.setText(_translate("Dialog", "Cafe"))
        self.checkBox_3.setText(_translate("Dialog", "Latte"))
        self.label_2.setText(_translate("Dialog", "Number of drink order"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def handleButtonClicked(self, Dialog):
        Dialog.accept()  # Close the dialog and emit accepted() signal
class VideoCam():
    def __init__(self, url):
        self.url = url

    def start(self):
      cap=cv2.VideoCapture(self.url)  
      face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
      # While loop to continuously fetching data from the Url
      while True:
          ret, frame = cap.read()
          gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
          for (x, y, w, h) in faces_detected:
              cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
              face_pic = frame[y:y+w, x:x+h]
              if cv2.waitKey(1) == ord("a"):
                  global potential_images
                  potential_images = []
                  cv2.imwrite("customer.jpg" , face_pic)
                  #cv2.imwrite("database_image\customer.jpg", face_pic)
                  #with open('database_image\customer.jpg', 'rb') as f:
                      #image_data_x = f.read()
                  #os.remove('database_image\customer.jpg')
                  # get all images from database 
                  database = DatabaseManager()
                  rows = database.get_all_images()
                  count = 0
                  for row in rows:
                    image_data = row[1]
                    image_id = row[0]
                    image = Image.open(io.BytesIO(image_data))
                    image.save('database_image\\'+str(image_id) + '.jpg')
                    count += 1

                  # find all image from database:
                  try:
                    dfs = DeepFace.find(img_path = "customer.jpg", db_path = "database_image", enforce_detection = False)
                    for i in dfs:
                      potential_images.append(i["identity"][0])
                  except ValueError: 
                    print("NO IMAGE match")

                  if (len(potential_images) > 0):
                     window = ImageWindow(potential_images)
                     window.exec_()
                     return cv2.destroyAllWindows()
                  else: 
                     with open('customer.jpg', 'rb') as f:
                        image_data = f.read()
                     database.add_image(image_data)                          
                     file_path = 'database_image\\representations_vgg_face.pkl'  # Replace with the actual file path
                     try:
                        os.remove(file_path)
                        print(f"File '{file_path}' successfully removed.")
                     except FileNotFoundError:
                          print(f"File '{file_path}' not found.")
                     except PermissionError:
                          print(f"Permission denied to remove file '{file_path}'.")
                     except Exception as e:
                          print(f"An error occurred while removing file '{file_path}': {e}")

                     customer_informations = DeepFace.analyze(img_path = "customer.jpg", 
                            actions = ['age', 'gender', 'race'], enforce_detection=False
                      )
                     image_id = database.get_image_id_by_binary(image_data)
                     print(image_id)
                     Dialog = QtWidgets.QDialog()
                     ui = Ui_Dialog()
                     ui.setupUi(Dialog)
                     ui.pushButton.clicked.connect(Dialog.accept)  # Connect button's clicked signal to accept() slot

                     result = Dialog.exec_()  # Store the result of the exec_() method
                     chocolate = 0
                     cafe = 0
                     latte = 0
                     name = ""
                     if result == QtWidgets.QDialog.Accepted:
                        print(ui.lineEdit.text())
                        name = ui.lineEdit.text()
                        if (ui.checkBox.isChecked()):
                           chocolate = ui.spinBox.value()
                        if (ui.checkBox_2.isChecked()):
                           cafe = ui.spinBox.value()
                        if (ui.checkBox_3.isChecked()):
                           latte = ui.spinBox.value()
                        print(chocolate)
                        print(cafe)
                        print(latte)
                             
                     Dialog.close()  # Close the dialog form

                     # Extract information
                     age = customer_informations[0]['age']
                     gender = max(customer_informations[0]['gender'], key=customer_informations[0]['gender'].get)
                     race = max(customer_informations[0]['race'], key=customer_informations[0]['race'].get)
                     current_time = datetime.datetime.now()
                     month = current_time.month 
                     database.insert_order(month, chocolate, cafe, latte, chocolate*35 + cafe * 30 + latte*40)
                     database.insert_customer(name, age, gender,race,chocolate,cafe,latte,int(image_id)) 
                     image = Image.open(io.BytesIO(image_data))
                     image.save('profile_image\\'+str(image_id) + '.jpg')
                     
                     # Put the id in the profile folder.
                     return cv2.destroyAllWindows()
                    
          resized_img = cv2.resize(frame, (1000, 700))
          cv2.imshow('Camera', resized_img)
          if cv2.waitKey(1) == ord("z"):
              break
      cv2.destroyAllWindows()
      
