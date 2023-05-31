import os
import sys

#from ui_interface import *
from ui_interface_2 import *
import rc_icons
from Custom_Widgets.Widgets import *

from PySide2 import *
from database import DatabaseManager
from camera import VideoCam, Ui_Dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from analyze import analyzer
import datetime


class CameraConnectWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CameraConnectWindow, self).__init__(parent)
        self.setWindowTitle("Camera Connection")
        self.resize(400, 200)
        
        layout = QtWidgets.QVBoxLayout(self)
        self.url_label = QtWidgets.QLabel("Camera URL:")
        layout.addWidget(self.url_label)
        self.url_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.url_edit)
        self.connect_button = QtWidgets.QPushButton("Connect")
        layout.addWidget(self.connect_button)
        
        self.connect_button.clicked.connect(self.connect_camera)

    def connect_camera(self):
        url = self.url_edit.text()
        video_cam = VideoCam(url)
        video_cam.start()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.array_figure = []
        self.array_canvas = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()
        self.ui.settingBtn.clicked.connect(lambda:self.ui.CenterMenuContainer.expandMenu())
        self.ui.InfoBtn.clicked.connect(lambda:self.ui.CenterMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda:self.ui.CenterMenuContainer.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda:self.ui.CenterMenuContainer.collapseMenu())

        #self.ui.profileMenuBtn.clicked.connect(lambda:self.ui.rightMenuContainer.expandMenu())
        #self.ui.moreMenuBtn.clicked.connect(lambda:self.ui.rightMenuContainer.expandMenu())
        #self.ui.moreMenuBtn.clicked.connect(self.start_video_cam)
        self.ui.profileMenuBtn.clicked.connect(self.open_profile_dialog)
        self.ui.closeRightMenu.clicked.connect(lambda:self.ui.rightMenuContainer.collapseMenu())
        self.ui.moreMenuBtn.clicked.connect(self.open_camera_window)
        self.ui.homeBtn.clicked.connect(self.display_home_page)

        self.ui.closeNotificationBtn.clicked.connect(lambda:self.ui.popupNotificationContainer.collapseMenu())
        self.ui.dataAnalysysBtn.clicked.connect(self.display_analyzer_page)
        self.ui.label_5.mousePressEvent = lambda event: self.refresh()
        self.ui.add_order.mousePressEvent = lambda event: self.open_order_form()
        self.ui.reportsBtn.clicked.connect(self.openReport)

        # add figure layout
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.array_figure.append(self.figure)
        self.array_canvas.append(self.canvas)
        self.ui.verticalLayout_17.addWidget(self.canvas)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.array_figure.append(self.figure)
        self.array_canvas.append(self.canvas)
        self.ui.verticalLayout_17.addWidget(self.canvas)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.array_figure.append(self.figure)
        self.array_canvas.append(self.canvas)
        self.ui.verticalLayout_17.addWidget(self.canvas)

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.array_figure.append(self.figure)
        self.array_canvas.append(self.canvas)
        self.ui.verticalLayout_18.addWidget(self.canvas)



    def openReport(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_8)
        analyze = analyzer()
        dic = analyze.year_analyze()
        width = 0.2
        x = range(12)
        ax = self.array_figure[3].add_subplot(111)
        months = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12']
        ax.bar(x, dic['chocolate'], width, color='blue', label='Cafe')
        ax.bar([i + width for i in x], dic['latte'], width, color='orange', label='Latte')
        ax.bar([i + 2 * width for i in x], dic['cafe'], width, color='green', label='Coffee')

        ax.set_xlabel('Months')
        ax.set_ylabel('Consumption')
        ax.set_title('Drink Consumption by Month')
        ax.set_xticks([i + width for i in x])
        ax.set_xticklabels(months)
        ax.legend()
        self.array_figure[3].tight_layout()

            # Refresh the canvas
        self.array_canvas[3].draw()
        
        

    def refresh(self):
        file_list = os.listdir("profile_image")
        for file_name in file_list:
            os.remove("profile_image\\" + file_name)
        
        if (len(self.array_figure) > 0):
            for i in self.array_figure:
                if (i.axes):
                    i.axes[0].remove()

                self.ui.name.setText("Name: ")
        self.ui.age.setText("Age: ")
        self.ui.gender.setText("Gender: ")
        self.ui.race.setText("Race: ")
        self.ui.chocolate.setText("Number of chocolate: ")
        self.ui.cafe.setText("Number of cafe: ")
        self.ui.latte.setText("Number of latte: ")
        self.ui.picture.setPixmap(None)
    
    def open_order_form(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.pushButton.clicked.connect(Dialog.accept) 
        result = Dialog.exec_()  # Store the result of the exec_() method
        chocolate = 0
        cafe = 0
        latte = 0
        if result == QtWidgets.QDialog.Accepted:
            if (ui.checkBox.isChecked()):
                chocolate = ui.spinBox.value()
            if (ui.checkBox_2.isChecked()):
                cafe = ui.spinBox.value()
            if (ui.checkBox_3.isChecked()):
                latte = ui.spinBox.value()

        # get the id
        file_list = os.listdir("profile_image")
        for file_name in file_list:
            id = os.path.splitext(file_name)[0]

        current_time = datetime.datetime.now()
        database = DatabaseManager()
        database.update_customer_drink(chocolate, latte, cafe, id)
        database.insert_order(current_time.month, chocolate, cafe, latte, 35 * chocolate + 40 * latte + 30 * cafe)
        self.ui.money.setText("Money: " + str(35 * chocolate + 40 * latte + 30 * cafe))
        self.display_home_page()
        Dialog.close()

                

    def open_camera_window(self):
        camera_window = CameraConnectWindow(self)
        camera_window.exec_()
    
    def open_profile_dialog(self):
        database = DatabaseManager()
        file_list = os.listdir("profile_image")

        for file_name in file_list:
            id = os.path.splitext(file_name)[0]
        print(id)
        print(type(int(id)))
        #with open("database_image\\output.jpg", 'rb') as f:
          #image_data = f.read()
        informations = database.get_customer_information_by_id(int(id))
        self.ui.name.setText("Name: "+ str(informations[0][0]))
        self.ui.age.setText("Age: "+ str(informations[0][1]))
        self.ui.gender.setText("Gender: "+ str(informations[0][2]))
        self.ui.race.setText("Race: "+ str(informations[0][3]))
        self.ui.chocolate.setText("Number of chocolate: "+ str(informations[0][4]))
        self.ui.cafe.setText("Number of cafe: "+ str(informations[0][5]))
        self.ui.latte.setText("Number of latte: "+ str(informations[0][6]))
        pixmap = QPixmap("profile_image\\" + str(id) + ".jpg")
        self.ui.picture.setPixmap(pixmap)

    def display_home_page(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_6)
        database = DatabaseManager()
        file_list = os.listdir("profile_image")
        if (len(file_list) > 0):
            for file_name in file_list:
                id = os.path.splitext(file_name)[0]
            print(id)
            print(type(int(id)))
            #with open("database_image\\output.jpg", 'rb') as f:
            #image_data = f.read()
            informations = database.get_customer_information_by_id(int(id))
            self.ui.name.setText("Name: "+ str(informations[0][0]))
            self.ui.age.setText("Age: "+ str(informations[0][1]))
            self.ui.gender.setText("Gender: "+ str(informations[0][2]))
            self.ui.race.setText("Race: "+ str(informations[0][3]))
            self.ui.chocolate.setText("Number of chocolate: "+ str(informations[0][4]))
            self.ui.cafe.setText("Number of cafe: "+ str(informations[0][5]))
            self.ui.latte.setText("Number of latte: "+ str(informations[0][6]))
            pixmap = QPixmap("profile_image\\" + str(id) + ".jpg")
            self.ui.picture.setPixmap(pixmap)
    def display_analyzer_page(self):
        file_list = os.listdir("profile_image")
        if (len(file_list) > 0):
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_7)
            for file_name in file_list:
                id = os.path.splitext(file_name)[0]

            # get the id
            file_list = os.listdir("profile_image")
            for file_name in file_list:
                id = os.path.splitext(file_name)[0]
            # get the customer information to analyze
            informations = database.get_customer_information_by_id(int(id))
            
            # Piechart gender
            Analyze = analyzer()
            gender_arr = Analyze.genderAnalyzer()
            gender = str(informations[0][2])
            Gender = gender_arr[gender]
            if (len(Gender) > 0):     
                ax = self.array_figure[0].add_subplot(111)
                labels = ['Chocolate', 'Latte', 'Cafe']
                sizes = Gender
                ax.pie(sizes, labels=labels, autopct='%1.1f%%')
                ax.set_title(gender + ' Favorite Drink')
                legend = ax.legend(title='Drink Type', loc='upper right')
                legend.set_title('Legend Description')

            # Adjust the layout
            self.array_figure[0].tight_layout()

            # Refresh the canvas
            self.array_canvas[0].draw()

            # Age PieChart

            age_arr = Analyze.ageAnalyzer()
            age = int(informations[0][1])
            age_group = ""
            if (age >= 0 and age <= 18): 
                age_group = "young"
            elif (age >= 19 and age <= 30):
                age_group = "middle"
            else: age_group = "old"
            if (len(age_arr[age_group]) > 0):
                ax = self.array_figure[1].add_subplot(111)
                labels = ['Chocolate', 'Latte', 'Cafe']
                sizes = Gender
                ax.pie(sizes, labels=labels, autopct='%1.1f%%')
                ax.set_title(age_group.title() + ' Age Group' + ' Favorite Drink')
                legend = ax.legend(title='Drink Type', loc='upper right')
                legend.set_title('Legend Description')

            self.array_figure[1].tight_layout()

            # Refresh the canvas
            self.array_canvas[1].draw()

            # Race Pie Chart

            race_arr = Analyze.raceAnalyzer()
            race = str(informations[0][3])
            if (len(race_arr[race]) > 0):
                ax = self.array_figure[2].add_subplot(111)
                labels = ['Chocolate', 'Latte', 'Cafe']
                sizes = Gender
                ax.pie(sizes, labels=labels, autopct='%1.1f%%')
                ax.set_title(race.title() + ' Favorite Drink')
                legend = ax.legend(title='Drink Type', loc='upper right')
                legend.set_title('Legend Description')

            self.array_figure[2].tight_layout()

            self.array_canvas[2].draw()
                
        else: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_7)


   
if __name__ == "__main__":
    database = DatabaseManager()
    database.create_customer_database()
    database.create_images_database()
    database.create_order_database()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


    