# -*- coding: utf-8 -*-
import psutil
import datetime
import schedule
import time
import win32serviceutil
import win32service
import win32event

cpu = {'user' : 0, 'system' : 0, 'idle' : 0, 'percent' : 0}
mem = {'total' : 0, 'avaiable' : 0, 'percent' : 0, 'used' : 0, 'free' : 0}
 
class ProcessPythonService(win32serviceutil.ServiceFramework):

    _svc_name_ = "ProcessPythonService"
    _svc_display_name_ = "The Process Python Service"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
 
    def SvcDoRun(self):
        schedule.every(5).minutes.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def get_cpu_info(self):
        cpu_times = psutil.cpu_times()
        cpu['user'] = cpu_times.user
        cpu['system'] = cpu_times.system
        cpu['idle'] = cpu_times.idle
        cpu['percent'] = psutil.cpu_percent(interval=2)

    def get_mem_info(self):
        mem_info = psutil.virtual_memory()
        mem['total'] = mem_info.total
        mem['available'] = mem_info.available
        mem['percent'] = mem_info.percent
        mem['used'] = mem_info.used
        mem['free'] = mem_info.free

    def job(self):
        print("I'm working...")
        self.get_cpu_info()
        self.get_mem_info()
        file = open('C:\Users\Administrator\Desktop\ProcessManagement_'+datetime.datetime.now().strftime('%Y%m%d')+'.txt', 'a')
        file.write('cpu status ' + str(cpu) + ' at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        file.write('memory status ' + str(mem) + ' at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        file.write('\n')
        file.close()

if __name__=='__main__':
    win32serviceutil.HandleCommandLine(ProcessPythonService)

