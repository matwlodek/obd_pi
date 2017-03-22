import cad
import mysql_connection as mc
# run only once!
# import mysql_dtc_database as mdd
# mdd.dtc_database_creator()
mc.dtc_check_db('P0001')
cad.start_screen()
cad.check_cable()
cad.main_menu()
