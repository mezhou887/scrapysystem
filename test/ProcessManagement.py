# -*- coding: utf-8 -*-
import psutil
import datetime
import schedule
import time
cpu = {'user' : 0, 'system' : 0, 'idle' : 0, 'percent' : 0}
mem = {'total' : 0, 'avaiable' : 0, 'percent' : 0, 'used' : 0, 'free' : 0}


def get_cpu_info():
    cpu_times = psutil.cpu_times()
    cpu['user'] = cpu_times.user
    cpu['system'] = cpu_times.system
    cpu['idle'] = cpu_times.idle
    cpu['percent'] = psutil.cpu_percent(interval=2)
    
def get_mem_info():
    mem_info = psutil.virtual_memory()
    mem['total'] = mem_info.total
    mem['available'] = mem_info.available
    mem['percent'] = mem_info.percent
    mem['used'] = mem_info.used
    mem['free'] = mem_info.free

def job():
    print("I'm working...")
    get_cpu_info()
    get_mem_info()
    file = open('C:\Users\Administrator\Desktop\ProcessManagement_'+datetime.datetime.now().strftime('%Y%m%d')+'.txt', 'a')
    file.write('cpu status ' + str(cpu) + ' at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    file.write('memory status ' + str(mem) + ' at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    file.write('\n')
    file.close()


if __name__ == '__main__':
    schedule.every(5).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

