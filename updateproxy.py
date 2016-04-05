# -*- coding: utf-8 -*-
import pymysql
import urllib2

class Proxy(object):
        
    def query(self, proxyType):
        if 'simple' == proxyType:
            link = 'http://www.baidu.com';
        else:
            link = 'http://www.google.com';
        
        pymysql.install_as_MySQLdb();
        output = open('misc/proxy.py', 'w');
        conn = pymysql.connect(host='192.168.0.27', port=3306, user='mezhou887', passwd='Admin1234#', db='quartz');
        cur = conn.cursor()
        
        output.write('HTTPPROXIES = ['+'\n');
        cur.execute("SELECT IPADDRESS, PORT FROM quartz.data_proxy where upper(type) = 'HTTP' order by dealdate desc ");
        for r in cur:
            if self.test(r[0]+':'+r[1], link, 'http'):
                output.write('{"ip_port": "'+r[0]+':'+r[1]+'"},'+'\n');
        output.writelines(']'+'\n\n');
        
        output.write('HTTPSPROXIES = ['+'\n');
        cur.execute("SELECT IPADDRESS, PORT FROM quartz.data_proxy where upper(type) = 'HTTPS' order by dealdate desc ");
        for r in cur:
            if self.test(r[0]+':'+r[1], link, 'https'):
                output.write('{"ip_port": "'+r[0]+':'+r[1]+'"},'+'\n');
        output.writelines(']'+'\n\n');
            
        cur.close();
        conn.close();
        output.close();

    # 不确定这个代理写法是否正确或网站提供的代理是正确的
    def test(self, ipaddress, link, conntype):
        print ipaddress, link, conntype;
        try:
            proxy = urllib2.ProxyHandler({conntype: ipaddress});
            opener = urllib2.build_opener(proxy);
            urllib2.install_opener(opener);
            response = urllib2.urlopen(link); 
            print response.read();
            return True;           
        except Exception,ex:
            print Exception,":",ex;
            return False;
    
proxy = Proxy();
proxy.query('simple');