#! /bin/bash
export PATH=$PATH:/usr/local/bin
cd /Users/mezhou887/Document/scrapysystem/release/cnbeta
nohup scrapy crawl cnbeta_base >> cnbeta_cron.log 2>&1 &