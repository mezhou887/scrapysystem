/Users/zhoumaoen/redis/bin/redis-cli shutdown  &
kill `ps -ef | grep mongodb | grep -v grep | awk '{print $2}'` &
kill `ps -ef | grep redis | grep -v grep | awk '{print $2}'` &
kill `ps -ef | grep scrapyd | grep -v grep | awk '{print $2}'` &
