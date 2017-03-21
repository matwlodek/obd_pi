import mysql.connector

mysql_conn = mysql.connector.connect(user='obd_pi', password='ELM327', host='127.0.0.1', database='obd', port='3306')
