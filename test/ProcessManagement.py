# -*- coding: utf-8 -*-
import psutil
import datetime
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cpu = {'user' : 0, 'system' : 0, 'idle' : 0, 'percent' : 0}
mem = {'total' : 0, 'avaiable' : 0, 'percent' : 0, 'used' : 0, 'free' : 0}

receivers = 'mezhou887@foxmail.com'

MAIL_USER = '1033738034@qq.com'
MAIL_PASS = 'ghyftlmoejsgbeai'


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

def send_mail():
    print("I'm working...")
    message = MIMEMultipart()
    message['From'] = '1033738034@qq.com'
    message['To'] =  'mezhou887@foxmail.com'
    message['Subject'] = '每日电脑状态'
    
    message.attach(MIMEText('我的电脑状态', 'plain', 'utf-8'))
    
    lastDate = datetime.date.today() - datetime.timedelta(days=1)
    filename = 'ProcessManagement_'+lastDate.strftime('%Y%m%d')+'.txt'
    att = MIMEText(open('C:/Users/Administrator/Desktop/'+filename, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=' + filename
    message.attach(att)
    
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(MAIL_USER,MAIL_PASS)
        server.sendmail(message['from'], message['to'],message.as_string())
        server.quit()
        print "Success: 邮件发送成功"
    except smtplib.SMTPException,ex:
        print ex
        print "Error: 无法发送邮件"
    

if __name__ == '__main__':
    schedule.every(5).minutes.do(job)
    schedule.every().day.at("00:15").do(send_mail)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

