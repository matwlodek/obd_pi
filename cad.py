import time
import pifacecad
from pifacecad.tools.question import LCDQuestion
import obd_connection as oc


cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.clear()


def start_screen():
    cad.lcd.set_cursor(5, 0)
    cad.lcd.cursor_off()
    cad.lcd.write("OBD PI")
    time.sleep(3)
    cad.lcd.clear()
    cad.lcd.set_cursor(0, 0)
    cad.lcd.cursor_off()
    cad.lcd.write("Mateusz")
    cad.lcd.set_cursor(0, 1)
    cad.lcd.cursor_off()
    cad.lcd.write("Wlodarczyk")
    time.sleep(2)
    cad.lcd.clear()
    cad.lcd.set_cursor(0, 0)
    cad.lcd.cursor_off()
    cad.lcd.write("Poznan")
    cad.lcd.set_cursor(0, 1)
    cad.lcd.cursor_off()
    cad.lcd.write("University")
    time.sleep(2)
    cad.lcd.clear()
    cad.lcd.set_cursor(0, 0)
    cad.lcd.cursor_off()
    cad.lcd.write("of Technology")
    cad.lcd.set_cursor(0, 1)
    cad.lcd.cursor_off()
    cad.lcd.write("2017")
    time.sleep(2)
    cad.lcd.clear()
    return


def main_menu():
    question = LCDQuestion(question="*MAIN MENU*", answers=['START', 'DTC', 'MY VIN'])
    result = question.ask()
    if result == 0:
        cad.lcd.clear()
        # TO DO
        # ASYNC OBD
        # CAD SHOW DATA WITH SCROLL OPTION / SHOW NEXT SCREEN
        # MYSQL DATA INJECTOR
    if result == 1:
        cad.lcd.clear()
        cad.lcd.set_cursor(0, 0)
        cad.lcd.cursor_off()
        cad.lcd.write('DIAGNOSTIC TROUBLE CODE')
        cad.lcd.set_cursor(0, 1)
        cad.lcd.cursor_off()
        cad.lcd.write(oc.mode3())
    if result == 2:
        cad.lcd.clear()
        cad.lcd.set_cursor(0, 0)
        cad.lcd.cursor_off()
        cad.lcd.write('MY VIN IS:')
        cad.lcd.set_cursor(0, 1)
        cad.lcd.cursor_off()
        cad.lcd.write(oc.vin())
    return


def check_serial_port():
    cad.lcd.set_cursor(0, 0)
    cad.lcd.cursor_off()
    cad.lcd.write("Serial device at")
    cad.lcd.set_cursor(0, 1)
    cad.lcd.cursor_off()
    cad.lcd.write(oc.serial_port())
    time.sleep(3)
    return


def check_cable():
    while True:
        question = LCDQuestion(question="Cable connected?", answers=['Yes', 'No'])
        result = question.ask()
        if result==0:
            break
        if result==1:
            cad.lcd.clear()
            cad.lcd.set_cursor(0, 0)
            cad.lcd.cursor_off()
            cad.lcd.write("Connect OBD2")
            cad.lcd.set_cursor(0, 1)
            cad.lcd.cursor_off()
            cad.lcd.write("cable now")
            time.sleep(3)
            cad.lcd.clear()
            cad.lcd.set_cursor(0, 0)
            cad.lcd.cursor_off()
            cad.lcd.write("Waiting...")
            for x in range(0, 16, 1):
                cad.lcd.set_cursor(x, 1)
                cad.lcd.cursor_off()
                cad.lcd.write("*")
                time.sleep(0.5)
            cad.lcd.clear()
            cad.lcd.set_cursor(0, 0)
            cad.lcd.cursor_off()
    return

