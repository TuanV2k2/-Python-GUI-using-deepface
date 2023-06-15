from database import DatabaseManager
import sqlite3
from datetime import datetime
class analyzer:
    def __init__(self):
        pass

    def genderAnalyzer(self):
        gender_arr = {}
        gender_arr["Man"] = []
        gender_arr["Woman"] = []
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE gender = ?", ("Man",))
        total_chocolate_man = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE gender = ?", ("Man",))
        total_latte_man = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE gender = ?", ("Man",))
        total_cafe_man = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE gender = ?", ("Woman",))
        total_chocolate_woman = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE gender = ?", ("Woman",))
        total_latte_woman = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE gender = ?", ("Woman",))
        total_cafe_woman = cursor.fetchone()[0]
        conn.close()

        arr = []
        sum = total_chocolate_man + total_cafe_man + total_latte_man
        if (sum != 0):
            arr.append(total_chocolate_man / sum * 100) 
            arr.append(total_latte_man / sum * 100)
            arr.append(total_cafe_man / sum * 100)
            gender_arr["Man"] = arr
        else: print('Not engough data for Man')
        
        arr_2 = []
        sum = total_chocolate_woman + total_cafe_woman + total_latte_woman
        if (sum != 0):
            arr_2.append(total_chocolate_woman / sum * 100) 
            arr_2.append(total_latte_woman / sum * 100)
            arr_2.append(total_cafe_woman / sum * 100)
            gender_arr["Woman"] = arr_2
        else: print('Not engough data for Woman')
        return gender_arr
    def ageAnalyzer(self):
        arr_age_group = {}
        arr_age_group["young"] = []
        arr_age_group["middle"] = []
        arr_age_group["old"] = []
        
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE age BETWEEN ? AND ?", (0, 18))
        total_chocolate_young = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE age BETWEEN ? AND ?", (0, 18))
        total_latte_young = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE age BETWEEN ? AND ?", (0, 18))
        total_cafe_young = cursor.fetchone()[0]

        arr_young = []
        sum = total_cafe_young + total_chocolate_young + total_latte_young
        if sum != 0:
            arr_young.append(total_chocolate_young / sum * 100)
            arr_young.append(total_latte_young / sum * 100)
            arr_young.append(total_cafe_young / sum * 100)
            arr_age_group["young"] = arr_young
        else:
            print("Not enough data for age (0-18).")

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE age BETWEEN ? AND ?", (19, 30))
        total_chocolate_middle = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE age BETWEEN ? AND ?", (19, 30))
        total_latte_middle = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE age BETWEEN ? AND ?", (19, 30))
        total_cafe_middle = cursor.fetchone()[0]

        arr_middle = []
        sum = total_cafe_middle + total_chocolate_middle + total_latte_middle
        if sum != 0:
            arr_middle.append(total_chocolate_middle / sum * 100)
            arr_middle.append(total_latte_middle / sum * 100)
            arr_middle.append(total_cafe_middle / sum * 100)
            arr_age_group["middle"] = arr_middle
        else:
            print("Not enough data for age (19-30).")

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE age BETWEEN ? AND ?", (31, 100))
        total_chocolate_old = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE age BETWEEN ? AND ?", (31, 100))
        total_latte_old = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE age BETWEEN ? AND ?", (31, 100))
        total_cafe_old = cursor.fetchone()[0]

        arr_old = []
        sum = total_cafe_old + total_chocolate_old + total_latte_old
        if sum != 0:
            arr_old.append(total_chocolate_old / sum * 100)
            arr_old.append(total_latte_old / sum * 100)
            arr_old.append(total_cafe_old / sum * 100)
            arr_age_group["old"] = arr_old
        else:
            print("Not enough data for age (31-100).")

        conn.close()
        return arr_age_group

    def raceAnalyzer(self):
        arr_race_group = {}
        arr_race_group["asian"] = []
        arr_race_group["white"] = []
        arr_race_group["black"] = []
        arr_race_group["indian"] = []
        arr_race_group["latino hispanic"] = []
        arr_race_group["middle eastern"] = []

        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE race = ?", ("asian",))
        total_chocolate_asian = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE race = ?", ("asian",))
        total_latte_asian = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE race = ?", ("asian",))
        total_cafe_asian = cursor.fetchone()[0]

        arr_asian = []
        sum = total_cafe_asian + total_chocolate_asian + total_latte_asian
        if sum != 0:
            arr_asian.append(total_chocolate_asian / sum * 100)
            arr_asian.append(total_latte_asian / sum * 100)
            arr_asian.append(total_cafe_asian / sum * 100)
            arr_race_group["asian"] = arr_asian
        else:
            print("Not enough data for the Asian race.")

        # Repeat the same process for the remaining race categories

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE race = ?", ("white",))
        total_chocolate_white = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE race = ?", ("white",))
        total_latte_white = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE race = ?", ("white",))
        total_cafe_white = cursor.fetchone()[0]

        arr_white = []
        sum = total_cafe_white + total_chocolate_white + total_latte_white
        if sum != 0:
            arr_white.append(total_chocolate_white / sum * 100)
            arr_white.append(total_latte_white / sum * 100)
            arr_white.append(total_cafe_white / sum * 100)
            arr_race_group["white"] = arr_white
        else:
            print("Not enough data for the White race.")

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE race = ?", ("black",))
        total_chocolate_black = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE race = ?", ("black",))
        total_latte_black = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE race = ?", ("black",))
        total_cafe_black = cursor.fetchone()[0]

        arr_black = []
        sum = total_cafe_black + total_chocolate_black + total_latte_black
        if sum != 0:
            arr_black.append(total_chocolate_black / sum * 100)
            arr_black.append(total_latte_black / sum * 100)
            arr_black.append(total_cafe_black / sum * 100)
            arr_race_group["black"] = arr_black
        else:
            print("Not enough data for the Black race.")

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE race = ?", ("indian",))
        total_chocolate_indian = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE race = ?", ("indian",))
        total_latte_indian = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE race = ?", ("indian",))
        total_cafe_indian = cursor.fetchone()[0]

        arr_indian = []
        sum = total_cafe_indian + total_chocolate_indian + total_latte_indian
        if sum != 0:
            arr_indian.append(total_chocolate_indian / sum * 100)
            arr_indian.append(total_latte_indian / sum * 100)
            arr_indian.append(total_cafe_indian / sum * 100)
            arr_race_group["indian"] = arr_indian
        else:
            print("Not enough data for the Indian race.")

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE race = ?", ("latino hispanic",))
        total_chocolate_latino = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE race = ?", ("latino hispanic",))
        total_latte_latino = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE race = ?", ("latino hispanic",))
        total_cafe_latino = cursor.fetchone()[0]

        arr_latino = []
        sum = total_cafe_latino + total_chocolate_latino + total_latte_latino
        if sum != 0:
            arr_latino.append(total_chocolate_latino / sum * 100)
            arr_latino.append(total_latte_latino / sum * 100)
            arr_latino.append(total_cafe_latino / sum * 100)
            arr_race_group["latino hispanic"] = arr_latino
        else:
            print("Not enough data for the Latino/Hispanic race.")

        cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM customer WHERE race = ?", ("middle eastern",))
        total_chocolate_middle_eastern = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM customer WHERE race = ?", ("middle eastern",))
        total_latte_middle_eastern = cursor.fetchone()[0]
        cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM customer WHERE race = ?", ("middle eastern",))
        total_cafe_middle_eastern = cursor.fetchone()[0]

        arr_middle_eastern = []
        sum = total_cafe_middle_eastern + total_chocolate_middle_eastern + total_latte_middle_eastern
        if sum != 0:
            arr_middle_eastern.append(total_chocolate_middle_eastern / sum * 100)
            arr_middle_eastern.append(total_latte_middle_eastern / sum * 100)
            arr_middle_eastern.append(total_cafe_middle_eastern / sum * 100)
            arr_race_group["middle eastern"] = arr_middle_eastern
        else:
            print("Not enough data for the Middle Eastern race.")

        conn.close()
        return arr_race_group
    def year_analyze(self):
        drinks = {}
        drinks['chocolate'] = []
        drinks['latte'] = []
        drinks['cafe'] = []
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()
        arr = []
        arr_1 = []
        arr_2 = []
        for i in range(1, 13):
            cursor.execute("SELECT IFNULL(SUM(chocolate), 0) FROM orders WHERE month = ?", (i,))
            total_chocolate = cursor.fetchone()[0]
            arr.append(total_chocolate)
            cursor.execute("SELECT IFNULL(SUM(latte), 0) FROM orders WHERE month = ?", (i,))
            total_latte = cursor.fetchone()[0]
            arr_1.append(total_latte)
            cursor.execute("SELECT IFNULL(SUM(cafe), 0) FROM orders WHERE month = ?", (i,))
            total_cafe = cursor.fetchone()[0]
            arr_2.append(total_cafe)
        drinks["chocolate"] = arr
        drinks["latte"] = arr_1
        drinks["cafe"] = arr_2
        conn.close()
        return drinks
    
    def year_revenue(self):
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()
        arr = []

        for i in range(1, 13):
            cursor.execute("SELECT IFNULL(SUM(total_money), 0) FROM orders WHERE month = ?", (i,))
            total_money = cursor.fetchone()[0]
            arr.append(total_money)

        conn.close()
        return arr
    
    def get_order_history(self, customer_id):
        conn = sqlite3.connect('databases/customer.db')
        cursor = conn.cursor()
        cursor.execute("SELECT day, month,year, chocolate, latte, cafe from orders where customer_id = ?", (customer_id,))
        result = cursor.fetchall()
        sorted_table = sorted(result, key=date_key)
        order_history = []
        i = 1
        for row in sorted_table:
            dic = {}
            dic['order_number'] = i
            dic['chocolate'] = row[3]
            dic['latte'] = row[4]
            dic['cafe'] = row[5]
            i += 1
            order_history.append(dic)
        return order_history

def date_key(row):
    day,month,year,_,_,_ = row
    return datetime(year, month, day)


    
        
