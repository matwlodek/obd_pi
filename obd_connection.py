import obd

sync_conn = obd.OBD()


def serial_port():
    return obd.scan_serial()


def car_conn_status():
    return sync_conn.status()
