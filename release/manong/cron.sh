#! /bin/bash
export PATH=$PATH:/usr/local/bin
cd /Users/mezhou887/Document/scrapysystem/release/manong
nohup scrapy crawl manong >> manong_cron.log 2>&1 &