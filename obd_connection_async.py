import obd
import time

async_conn = obd.Async()

def new_rpm(r):
    return r.value

def rpm_async():
    async_conn.watch(obd.commands.RPM, callback=new_rpm)
    async_conn.start()
    time.sleep(5)
    async_conn.stop();


