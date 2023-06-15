import os
import sys

#from ui_interface import *
from ui_interface_2 import *
import rc_icons
from Custom_Widgets.Widgets import *

from PySide2 import *
from database import DatabaseManager
from camera import VideoCam, Ui_Dialog, OrderForm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from analyze import analyzer
from login import Ui_Form
import datetime

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 250)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/4856718.png"), QIcon.Normal, QIcon.Off)  # Replace "/path/to/icon.png" with the path to the icon in the resource file
        self.setWindowIcon(icon)
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            
            QLineEdit {
                background-color: white;
            }
            QPushButton {
                background-color: gray;
            }
        """)

        # Create widgets
        self.name_label = ('Name:')
        self.name_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.signup_button = QPushButton('Sign Up')

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect button signals to methods
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.signup)

    def login(self):
        name = self.name_input.text()
        password = self.password_input.text()

        # Add your login validation logic here
        # For demonstration purposes, let's assume the login is successful if the name and password are both "admin"
        if name == "admin" and password == "admin":
            self.open_main_form()
        else:
            print("Invalid login credentials!")

    def signup(self):
        name = self.name_input.text()
        password = self.password_input.text()
        # Add your signup logic here

    def open_main_form(self):
        self.hide()
        self.main_form = MainWindow()
        self.main_form.show()

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
        video_cam = VideoCam(url,self)
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

        self.ui.profileMenuBtn.clicked.connect(lambda:self.ui.rightMenuContainer.expandMenu())
        #self.ui.moreMenuBtn.clicked.connect(lambda:self.ui.rightMenuContainer.expandMenu())
        #self.ui.moreMenuBtn.clicked.connect(self.start_video_cam)
        #self.ui.profileMenuBtn.clicked.connect(self.open_profile_dialog)
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
        ax.bar(x, dic['chocolate'], width, color='blue', label='Chocolate')
        ax.bar([i + width for i in x], dic['latte'], width, color='orange', label='Latte')
        ax.bar([i + 2 * width for i in x], dic['cafe'], width, color='green', label='Cafe')

        ax.set_xlabel('Months')
        ax.set_ylabel('Consumption')
        ax.set_title('Drink Consumption by Month')
        ax.set_xticks([i + width for i in x])
        ax.set_xticklabels(months)
        ax.legend()

        self.array_canvas[3].draw()

        #revenue plot
        analyze = analyzer()
        arr = analyze.year_revenue()
        width = 0.2
        x = range(12)
        ax_1 = self.array_figure[4].add_subplot(111)
        months = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12']
        ax_1.bar(x, arr, width, color='gray', label='total_money')

        ax_1.set_xlabel('Months')
        ax_1.set_ylabel('Revenue')
        ax_1.set_title('Revenue by month')
        ax_1.set_xticks([i for i in x])
        ax_1.set_xticklabels(months)
        ax_1.legend()

        self.array_canvas[4].draw()

    def refresh(self):
        file_list = os.listdir("profile_image")
        for file_name in file_list:
            os.remove("profile_image\\" + file_name)
        
        if (len(self.array_figure) > 0):
            for i in self.array_figure:
                if (i.axes):
                    for plot in i.axes:
                        plot.remove()

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
        database.insert_order(current_time.day, current_time.month, current_time.year, chocolate, cafe, latte, 35 * chocolate + 40 * latte + 30 * cafe, id)
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
        if (len(self.array_figure) > 0):
            for i in self.array_figure:
                if (i.axes):
                    for plot in i.axes:
                        plot.remove()
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
            database = DatabaseManager()
            informations = database.get_customer_information_by_id(int(id))
            
            # Get the analyzed data
            Analyze = analyzer()
            gender_arr = Analyze.genderAnalyzer()
            gender = str(informations[0][2])
            Gender = gender_arr[gender]

            race_arr = Analyze.raceAnalyzer()
            race = str(informations[0][3])

            age_arr = Analyze.ageAnalyzer()
            age = int(informations[0][1])
            age_group = ""
            if (age >= 0 and age <= 18): 
                age_group = "young"
            elif (age >= 19 and age <= 30):
                age_group = "middle"
            else: age_group = "old"

            # get order_history
            order_history = Analyze.get_order_history(id)
            order_numbers = [order['order_number'] for order in order_history]
            chocolate_values = [order['chocolate'] for order in order_history]
            cafe_values = [order['cafe'] for order in order_history]
            latte_values = [order['latte'] for order in order_history]
            print(order_history)
            # Piechart gender

            if (len(Gender) > 0):     
                ax = self.array_figure[0].add_subplot(131)
                labels = ['Chocolate', 'Latte', 'Cafe']
                sizes = Gender
                colors = ["#808080", "#3498db", "#ff7f50"]
                pie = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors = colors)
                ax.set_title(gender + ' Favorite Drink')
                label_colors = {label: color for label, color in zip(labels, colors)}
                for label in pie[1]:
                    label.set_color(label_colors[label.get_text()]) 
                legend = ax.legend(title='Drink Type', loc='upper right', bbox_to_anchor=(1.7, 1))
                legend.set_title('Legend Description')

                # get top 3 drink:
                ranks = []
                for i in range(3):
                    id = Gender.index(max(Gender))
                    if (id == 0):
                        ranks.append("Chocolate")
                    elif id == 1: ranks.append("Latte")
                    else: ranks.append("Cafe")
                    Gender[id] = -1

                
                subplot = self.array_figure[0].add_subplot(132)
                subplot.text(0.5, 0.9, "Top 1: " + ranks[0], ha='center', va='center', fontsize=14)
                subplot.text(0.5, 0.5, "Top 2: " + ranks[1], ha='center', va='center', fontsize=14)
                subplot.text(0.5, 0.1, "Top 3: " + ranks[2], ha='center', va='center', fontsize=14)
                subplot.set_axis_off()

                trend_plot = self.array_figure[0].add_subplot(133)
                # Extract data for each drink type
                trend_plot.plot(order_numbers, chocolate_values, label='Chocolate')
                trend_plot.plot(order_numbers, cafe_values, label='Cafe')
                trend_plot.plot(order_numbers, latte_values, label='Latte')

                # Customize the plot
                trend_plot.set_xlabel('Order Number')
                trend_plot.set_ylabel('Values')
                trend_plot.set_title('Order History')
                trend_plot.legend()

                # Add a point at specific order numbers
                specific_order_numbers = [i for i in range(1, len(order_numbers) + 1)]  # Example list of specific order numbers
                for specific_order_number in specific_order_numbers:
                    if specific_order_number in order_numbers:
                        specific_index = order_numbers.index(specific_order_number)
                        specific_chocolate_value = chocolate_values[specific_index]
                        specific_cafe_value = cafe_values[specific_index]
                        specific_latte_value = latte_values[specific_index]
                        
                        trend_plot.scatter(specific_order_number, specific_chocolate_value, color='red', label='Specific Order')
                        trend_plot.scatter(specific_order_number, specific_cafe_value, color='red')
                        trend_plot.scatter(specific_order_number, specific_latte_value, color='red')

            # Adjust the layout

            # Refresh the canvas
            self.array_canvas[0].draw()

            # Age PieChart
            if (len(age_arr[age_group]) > 0):
                ax = self.array_figure[1].add_subplot(111)
                labels = ['Chocolate', 'Latte', 'Cafe']
                sizes = age_arr[age_group]
                colors = ["#808080", "#3498db", "#ff7f50"]
                pie = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
                label_colors = {label: color for label, color in zip(labels, colors)}
                for label in pie[1]:
                    label.set_color(label_colors[label.get_text()]) 

                ax.set_title(age_group.title() + ' Age Group' + ' Favorite Drink')
                legend = ax.legend(title='Drink Type', loc='upper right',  bbox_to_anchor=(1.7, 1))
                legend.set_title('Type of drink')

                ranks = []
                for i in range(3):
                    id = age_arr[age_group].index(max(age_arr[age_group]))
                    if (id == 0):
                        ranks.append("Chocolate")
                    elif id == 1: ranks.append("Latte")
                    else: ranks.append("Cafe")
                    age_arr[age_group][id] = -1
                
                subplot = self.array_figure[1].add_subplot(122)
                subplot.text(0.5, 0.9, "Top 1: " + ranks[0], ha='center', va='center', fontsize=14)
                subplot.text(0.5, 0.5, "Top 2: " + ranks[1], ha='center', va='center', fontsize=14)
                subplot.text(0.5, 0.1, "Top 3: " + ranks[2], ha='center', va='center', fontsize=14)
                subplot.set_axis_off()
                


            # Refresh the canvas
            self.array_canvas[1].draw()

            # Race Pie Chart
            if (len(race_arr[race]) > 0):
                ax = self.array_figure[2].add_subplot(111)
                labels = ['Chocolate', 'Latte', 'Cafe']
                colors = ["#808080", "#3498db", "#ff7f50"]
                sizes = race_arr[race]
                pie = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors = colors)
                label_colors = {label: color for label, color in zip(labels, colors)}
                for label in pie[1]:
                    label.set_color(label_colors[label.get_text()]) 
                ax.set_title(race.title() + ' Favorite Drink')
                legend = ax.legend(title='Drink Type', loc='upper right', bbox_to_anchor=(1.7, 1))
                legend.set_title('Type of drink')

                ranks = []
                for i in range(3):
                    id = race_arr[race].index(max(race_arr[race]))
                    if (id == 0):
                        ranks.append("Chocolate")
                    elif id == 1: ranks.append("Latte")
                    else: ranks.append("Cafe")
                    race_arr[race][id] = -1

                
                subplot = self.array_figure[2].add_subplot(122)
                subplot.text(0.5, 0.9, "Top 1: " + ranks[0], ha='center', va='center', fontsize=14)
                subplot.text(0.5, 0.5, "Top 2: " + ranks[1], ha='center', va='center', fontsize=14)
                subplot.text(0.5, 0.1, "Top 3: " + ranks[2], ha='center', va='center', fontsize=14)
                subplot.set_axis_off()

            self.array_canvas[2].draw()
                
        else: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_7)


   
if __name__ == "__main__":
    database = DatabaseManager()
    database.create_customer_database()
    database.create_images_database()
    database.create_order_database()
    database.create_accounts_table()
    database.create_manager_table()
    app = QtWidgets.QApplication(sys.argv)
    #window = MainWindow()
    Form = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.exec_()
    sys.exit(app.exec_())


    