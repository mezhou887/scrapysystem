# -*- coding: utf-8 -*-
import pymysql

if __name__ =="__main__":
    pymysql.install_as_MySQLdb();
    output = open('misc/proxy.py', 'w');
    conn = pymysql.connect(host='192.168.0.27', port=3306, user='mezhou887', passwd='Admin1234#', db='quartz');
    cur = conn.cursor()
    
    output.write('HTTPPROXIES = ['+'\n');
    cur.execute("SELECT IPADDRESS, PORT FROM quartz.data_proxy where upper(type) = 'HTTP' ");
    for r in cur:
        output.write('{"ip_port": "'+r[0]+':'+r[1]+'"},'+'\n');
    output.writelines(']'+'\n\n');
    
    output.write('HTTPSPROXIES = ['+'\n');
    cur.execute("SELECT IPADDRESS, PORT FROM quartz.data_proxy where upper(type) = 'HTTPS' ");
    for r in cur:
        output.write('{"ip_port": "'+r[0]+':'+r[1]+'"},'+'\n');
    output.writelines(']'+'\n\n');
        
    cur.close();
    conn.close();
    output.close();
