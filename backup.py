# -*- coding: utf-8 -*-
import commands,time

if __name__ =="__main__":
    # linux shell script： tar -zcvf cnbeta.tar.gz cnbeta
    s = 'cnbeta'
    command = 'tar -zcvf ' +s +  time.strftime("%Y%m%d%H%M%S", time.localtime()) +'.tar.gz ' + s
    commands.getstatusoutput(command)

