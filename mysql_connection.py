import mysql_connection_settings as mcs

cursor = mcs.mysql_conn.cursor()

query_dtc_check = ("SELECT technical_description FROM diagnostic_trouble_code_db "
                   "WHERE dtc_code LIKE %s")


def dtc_check_db(code):
    cursor.execute(query_dtc_check, (code,))
    for (technical_description) in cursor:
        print("{}".format(technical_description))
