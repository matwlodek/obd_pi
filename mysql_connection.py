import mysql_connection_settings as mcs

cursor = mcs.mysql_conn.cursor()

query_dtc_check = ("SELECT technical_description FROM diagnostic_trouble_code_db "
                   "WHERE dtc_code = %s")

def dtc_check_db():
    cursor.execute(query_dtc_check, 'P0001')
    cursor.close()
    return
