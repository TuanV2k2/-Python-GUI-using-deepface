
import sqlite3
class DatabaseManager():
    def __init__(self):
        pass
    
    def update_customer_drink(self, chocolate, latte, cafe, id):
        conn = sqlite3.connect("databases/customer.db")
        cursor = conn.cursor()
        # Retrieve the current number of drink orders for the customer
        cursor.execute("SELECT chocolate, latte,cafe FROM customer WHERE id=?", (id,))
        number_of_drink = cursor.fetchall()[0]
        previous_chocolate = number_of_drink[0]
        
        previous_latte = number_of_drink[1]
        previous_cafe = number_of_drink[2]

        # Increase the number of drink orders by 1
        new_chocolate = previous_chocolate + chocolate
        new_latte = previous_latte + latte
        new_cafe = previous_cafe + cafe

        # Update the customer's drink order count in the database
        cursor.execute("UPDATE customer SET chocolate=?, latte=?, cafe=? WHERE id=?", (new_chocolate, new_latte, new_cafe, id))
        conn.commit()
        conn.close()

    def get_image_id_by_binary(self, image_binary):
        conn = sqlite3.connect("databases/customer.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM images WHERE image = ?", (image_binary,))
        result = cursor.fetchone()
        conn.close()
        return result[0]

    def get_customer_information_by_id(self, image_id):
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, age, gender, race,chocolate, cafe, latte FROM customer WHERE image_id = ?", (image_id,))
        result = cursor.fetchall()
        conn.close()
        return result

    def insert_customer(self, name, age, gender, race, chocolate, cafe, latte, image_id):
        # Connect to the database file
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Insert the customer data into the customer table
        cursor.execute('INSERT INTO customer (name, age, gender, race, chocolate, cafe, latte, image_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (name, age, gender, race, chocolate, cafe, latte, image_id))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

    def remove_customer(self,customer_id):
        # Connect to the database file
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Delete the customer from the customer table based on the provided customer ID
        cursor.execute('DELETE FROM customer WHERE id = ?', (customer_id,))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()


    def create_images_database(self):
        # Connect to the database file (or create it if it doesn't exist)
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute SQL statement to create the images table
        cursor.execute('CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, image BLOB)')

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()


    def create_customer_database(self):
        # Connect to the database file (or create it if it doesn't exist)
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute SQL statement to create the customer table
        cursor.execute('CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, race TEXT, chocolate INTEGER, cafe INTEGER,latte INTEGER , image_id INTEGER, FOREIGN KEY (image_id) REFERENCES images(id))')

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

    def create_order_database(self):
        # Connect to the database file (or create it if it doesn't exist)
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute SQL statement to create the orders table
        cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY,day INTEGER, month INTEGER, year INTEGER,chocolate INTEGER, latte INTEGER, cafe INTEGER, total_money INTEGER, customer_id INTEGER, FOREIGN KEY (customer_id) REFERENCES customer(id))')

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()



    def insert_order(self,day, month, year, chocolate,cafe, latte, total_money, customer_id):
        # Connect to the database file
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        cursor.execute('INSERT INTO orders (day, month, year,chocolate, cafe, latte, total_money, customer_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (day, month, year,chocolate, cafe, latte, total_money, customer_id))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()
    

    def add_image(self, image_data):
        # Connect to the database file
        conn = sqlite3.connect('databases/customer.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Insert the image data into the images table
        cursor.execute('INSERT INTO images (image) VALUES (?)', (image_data,))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

    def get_all_images(self):
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * from images')
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def get_customer_id_by_image_id(self, image_id):
        conn = sqlite3.connect("databases/customer.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM customer WHERE image_id = ?", (image_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
    
    def get_orders_by_customer_id(self, customer_id):
        conn = sqlite3.connect("databases/customer.db")
        cursor = conn.cursor()

        cursor.execute('SELECT chocolate, latte, cafe, total_money FROM orders Where customer_id = ?', (customer_id,))
        result = cursor.fetchall()
        conn.close()
        return result 
    
    def create_accounts_table(self):
        conn = sqlite3.connect('databases/employee.db')

        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, name TEXT, password TEXT, image blob)')

        conn.commit()

        conn.close()

    def create_manager_table(self):
        conn = sqlite3.connect('databases/employee.db')

        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS login_history (id INTEGER PRIMARY KEY, day INTEGER, month INTEGER, year INTEGER, image blob, employee_id INTEGER,FOREIGN KEY (employee_id) REFERENCES accounts(id))')

        conn.commit()

        conn.close()


    def insert_employee(self, name, password, image):
        conn = sqlite3.connect('databases/employee.db')
        cursor = conn.cursor()
        
        # Insert the customer data into the customer table
        cursor.execute('INSERT INTO accounts (name, password, image) VALUES (?, ?, ?)', (name, password, image))

        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()
    
    def find_account(self, name, password):
        conn = sqlite3.connect('databases/employee.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id from accounts WHERE name = ? and password = ?', (name, password))

        # Commit the changes
        result = cursor.fetchone()

        # Close the connection
        conn.close()
        return result[0]

    def insert_employee_login(self, id, day, month, year, image):
        conn = sqlite3.connect('databases/employee.db')
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO login_history (employee_id, day, month, year, image) VALUES (?, ?, ?, ?, ?)', (id, day, month, year, image))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

    
    
    
    
    
    
    
    




