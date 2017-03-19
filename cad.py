import time

import pifacecad
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

import obd_connection as oc

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
        cad.lcd.write("Connecting...")
        for x in range(0, 16, 1):
            cad.lcd.set_cursor(x, 1)
            cad.lcd.cursor_off()
            cad.lcd.write("*")
            time.sleep(0.5)
        cad.lcd.clear()
        cad.lcd.set_cursor(0, 0)
        cad.lcd.cursor_off()
        cad.lcd.write(oc.car_conn_status())
        time.sleep(10)
        if oc.car_conn_status()!="Not Connected":
            break
    return
