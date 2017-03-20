import obd
import time

async_conn = obd.Async()


def new_status(status):  # Status since DTCs cleared
    return status.value


def new_fuel_status(fuel_status):  # Fuel System Status
    return fuel_status.value


def new_engine_load(engine_load):  # Calculated Engine Load
    return engine_load.value


def new_coolant_temp(coolant_temp):  # Engine Coolant Temperature
    return coolant_temp.value


def new_fuel_pressure(fuel_pressure):  # Fuel Pressure
    return fuel_pressure.value


def new_intake_pressure(intake_pressure):  # INTAKE_PRESSURE
    return intake_pressure.value


def new_rpm(rpm):  # Engine RPM
    return rpm.value


def new_speed(speed):  # Vehicle Speed
    return speed.value


def new_intake_temp(intake_temp):  # Intake Air Temp
    return intake_temp.value


def new_maf(maf):  # Air Flow Rate (MAF)
    return maf.value


def new_throttle_pos(throttle_pos):  # Throttle Position
    return throttle_pos.value


def new_oil_temp(oil_temp):  # Engine oil temperature
    return oil_temp.value

async_conn.watch(obd.commands.STATUS, callback=new_status)
async_conn.watch(obd.commands.FUEL_STATUS, callback=new_fuel_status)
async_conn.watch(obd.commands.ENGINE_LOAD, callback=new_engine_load)
async_conn.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temp)
async_conn.watch(obd.commands.FUEL_PRESSURE, callback=new_fuel_pressure)
async_conn.watch(obd.commands.INTAKE_PRESSURE, callback=new_intake_pressure)
async_conn.watch(obd.commands.RPM, callback=new_rpm)
async_conn.watch(obd.commands.SPEED, callback=new_speed)
async_conn.watch(obd.commands.INTAKE_TEMP, callback=new_intake_temp)
async_conn.watch(obd.commands.MAF, callback=new_maf)
async_conn.watch(obd.commands.THROTTLE_POS, callback=new_throttle_pos)
async_conn.watch(obd.commands.OIL_TEMP, callback=new_oil_temp)

async_conn.start()
time.sleep(60)
async_conn.stop()


