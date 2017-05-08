import pifacecad
import time
import obd_connection as oc
import mysql_connection as mc
from subprocess import call

cad = pifacecad.PiFaceCAD()

MONITOR = [
    {'name': 'STATUS', 'command': 'obd.commands.STATUS', 'id': 1},
    {'name': 'FUEL STATUS', 'command': 'obd.commands.FUEL_STATUS', 'id': 2},
    {'name': 'ENGINE LOAD', 'command': 'obd.commands.ENGINE_LOAD', 'id': 3},
    {'name': 'COOLANT TEMP', 'command': 'obd.commands.COOLANT_TEMP', 'id': 4},
    {'name': 'FUEL PRESSURE', 'command': 'obd.commands.FUEL_PRESSURE', 'id': 5},
    {'name': 'INTAKE PRESSURE', 'command': 'obd.commands.INTAKE_PRESSURE', 'id': 6},
    {'name': 'RPM', 'command': 'obd.commands.RPM', 'id': 7},
    {'name': 'SPEED', 'command': 'obd.commands.SPEED', 'id': 8},
    {'name': 'INTAKE TEMP', 'command': 'obd.commands.INTAKE_TEMP', 'id': 9},
    {'name': 'MAF', 'command': 'obd.commands.MAF', 'id': 10},
    {'name': 'THROTTLE POS', 'command': 'obd.commands.THROTTLE_POS', 'id': 11},
    {'name': 'OIL TEMP', 'command': 'obd.commands.OIL_TEMP', 'id': 12}
    ]


class Monitor(object):
    def __init__(self, name, command, monitor_id):
        self.name = name
        self.command = command
        self.monitor_id = monitor_id


class Display(object):
    def __init__(self, cad, monitors, monitor_index=0):
        self.cad = cad
        self.monitors = monitors
        self.monitor_index = monitor_index

    @property
    def current_monitor(self):
        return self.monitors[self.monitor_index]

    def next_monitor(self):
        self.monitor_index = (self.monitor_index + 1) % len(self.monitors)
        self.update_display()

    def previous_monitor(self):
        self.monitor_index = (self.monitor_index - 1) % len(self.monitors)
        self.update_display()

    def update_display(self):
        self.cad.lcd.clear()
        self.cad.lcd.set_cursor(0, 0)
        self.cad.lcd.write("{name}\n".format(name=self.monitors[self.monitor_index].name))
        self.cad.lcd.set_cursor(0, 1)
        self.cad.lcd.write("{command}\n".format(command=self.monitors[self.monitor_index].command))

    def start_screen(self):
        self.cad.lcd.backlight_on()
        self.cad.lcd.set_cursor(5, 0)
        self.cad.lcd.cursor_off()
        self.cad.lcd.write("OBD PI")
        time.sleep(3)
        self.cad.lcd.clear()
        self.cad.lcd.write("Mateusz\nWlodarczyk")
        time.sleep(2)
        self.cad.lcd.clear()
        self.cad.lcd.write("Poznan\nUniversity")
        time.sleep(2)
        self.cad.lcd.clear()
        self.cad.lcd.write("of Technology\n2017")
        time.sleep(2)
        self.cad.lcd.clear()

    def main_menu(self):
        self.cad.lcd.clear()
        self.cad.lcd.write('MAIN MENU  <|U|>\nS|D|V|B||OFF')

    def start(self):
        self.cad.lcd.clear()
        self.update_display()
    # TO DO
    # ASYNC OBD
    # CAD SHOW DATA WITH SCROLL OPTION / SHOW NEXT SCREEN
    # MYSQL DATA INJECTOR

    def dtc(self):
        self.cad.lcd.clear()
        self.cad.lcd.set_cursor(0, 0)
        self.cad.lcd.cursor_off()
        self.cad.lcd.write('YOUR DTC:')
        while True:
            try:
                self.cad.lcd.set_cursor(0, 1)
                self.cad.lcd.cursor_off()
                self.cad.lcd.write(str(oc.mode3()))
                time.sleep(5)
                if len(str(oc.mode3())) == 5:
                    time.sleep(5)
                    self.cad.lcd.clear()
                    self.cad.lcd.set_cursor(0, 0)
                    self.cad.lcd.cursor_off()
                    self.cad.lcd.write(str(oc.mode3()))
                    self.cad.lcd.set_cursor(0, 1)
                    self.cad.lcd.cursor_off()
                    self.cad.lcd.write(mc.dtc_check_db)
                    self.cad.lcd.move_right()
                break
            except AttributeError:
                self.cad.lcd.set_cursor(0, 1)
                self.cad.lcd.cursor_off()
                self.cad.lcd.write('error, no data')
                break

    def vin(self):
        self.cad.lcd.clear()
        self.cad.lcd.set_cursor(0, 0)
        self.cad.lcd.cursor_off()
        self.cad.lcd.write('YOUR VIN:')
        while True:
            try:
                self.cad.lcd.set_cursor(0, 1)
                self.cad.lcd.cursor_off()
                self.cad.lcd.write(str(oc.vin()))
                break
            except AttributeError:
                self.cad.lcd.set_cursor(0, 1)
                self.cad.lcd.cursor_off()
                self.cad.lcd.write('error, no data')
                break

    def off(self):
        self.cad.lcd.clear()
        self.cad.lcd.write('System shutting \ndown...')
        time.sleep(2)
        self.cad.lcd.cursor_off()
        self.cad.lcd.backlight_off()
        call("sudo shutdown -h now", shell=True)


def update_pin_text(event):
    event.chip.lcd.write(str(event.pin_num))
    choice = event.pin_num
    if choice == 0:
        display.start()
    if choice == 1:
        display.dtc()
    if choice == 2:
        display.vin()
    if choice == 3:
        display.main_menu()
    if choice == 4:
        display.off()
    if choice == 5:
        display.update_display()
    if choice == 6:
        display.previous_monitor()
    if choice == 7:
        display.next_monitor()

if __name__ == "__main__":
    monitors = \
        [Monitor(s['name'], s['command'], s['id']) for s in MONITOR]
    global display
    display = Display(cad, monitors)
    display.start_screen()
    display.main_menu()
    listener = pifacecad.SwitchEventListener(chip=cad)
    for i in range(8):
        listener.register(i, pifacecad.IODIR_ON, update_pin_text)
    listener.activate()